-- database_setup_2026.sql - PostgreSQL 17 + pgvector

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS btree_gin;

-- Drop existing tables (for clean setup)
DROP TABLE IF EXISTS legal_documents_2026 CASCADE;
DROP TABLE IF EXISTS knowledge_graph_2026 CASCADE;
DROP TABLE IF EXISTS document_chunks_2026 CASCADE;

-- Main documents table
CREATE TABLE legal_documents_2026 (
    id SERIAL PRIMARY KEY,
    doc_id VARCHAR(255) UNIQUE NOT NULL,
    source VARCHAR(500) NOT NULL,
    title TEXT,
    content TEXT NOT NULL,
    
    -- Dense embeddings (MixedBread-AI 1024-dim)
    embedding vector(1024),
    
    -- Metadata
    doc_type VARCHAR(100),  -- 'constitution', 'act', 'judgment', 'article'
    jurisdiction VARCHAR(100),
    year INTEGER,
    category VARCHAR(100),
    tags TEXT[],
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    -- Full-text search
    content_tsvector tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED
);

-- Adaptive chunks table
CREATE TABLE document_chunks_2026 (
    id SERIAL PRIMARY KEY,
    chunk_id VARCHAR(255) UNIQUE NOT NULL,
    doc_id VARCHAR(255) REFERENCES legal_documents_2026(doc_id) ON DELETE CASCADE,
    
    -- Content
    chunk_text TEXT NOT NULL,
    chunk_size INTEGER,
    chunk_index INTEGER,
    
    -- Dense embeddings
    embedding vector(1024),
    
    -- ColBERT multi-vector embeddings (up to 256 tokens, 128-dim each)
    colbert_embeddings vector(128)[],
    
    -- Context
    prev_chunk_id VARCHAR(255),
    next_chunk_id VARCHAR(255),
    parent_section TEXT,
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT NOW()
);

-- Knowledge graph for GraphRAG
CREATE TABLE knowledge_graph_2026 (
    id SERIAL PRIMARY KEY,
    entity_id VARCHAR(255) UNIQUE NOT NULL,
    entity_type VARCHAR(100) NOT NULL,  -- 'article', 'right', 'restriction', 'case'
    entity_name TEXT NOT NULL,
    
    -- Embedding
    embedding vector(1024),
    
    -- Relationships (stored as JSONB for flexibility)
    relationships JSONB,
    -- Example: [
    --   {"type": "RELATES_TO", "target": "article_19", "weight": 0.9},
    --   {"type": "RESTRICTS", "target": "freedom_of_speech", "weight": 0.7}
    -- ]
    
    -- Metadata
    source_doc_id VARCHAR(255),
    metadata JSONB,
    
    created_at TIMESTAMP DEFAULT NOW()
);

-- Query history (for analysis and improvement)
CREATE TABLE query_history_2026 (
    id SERIAL PRIMARY KEY,
    query_text TEXT NOT NULL,
    query_embedding vector(1024),
    
    -- Results
    top_doc_ids TEXT[],
    answer TEXT,
    
    -- Performance
    retrieval_time_ms FLOAT,
    generation_time_ms FLOAT,
    total_time_ms FLOAT,
    
    -- Safety
    hallucination_score FLOAT,
    risk_level VARCHAR(50),
    is_safe BOOLEAN,
    
    -- User feedback (if available)
    feedback_score INTEGER,
    feedback_comment TEXT,
    
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for performance

-- Vector indexes (HNSW for fast ANN search)
CREATE INDEX idx_docs_embedding_2026 
ON legal_documents_2026 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

CREATE INDEX idx_chunks_embedding_2026 
ON document_chunks_2026 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

CREATE INDEX idx_graph_embedding_2026 
ON knowledge_graph_2026 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- Full-text search index
CREATE INDEX idx_docs_fts_2026 
ON legal_documents_2026 
USING GIN (content_tsvector);

-- Regular indexes
CREATE INDEX idx_docs_doc_id_2026 ON legal_documents_2026(doc_id);
CREATE INDEX idx_docs_year_2026 ON legal_documents_2026(year);
CREATE INDEX idx_docs_category_2026 ON legal_documents_2026(category);

CREATE INDEX idx_chunks_doc_id_2026 ON document_chunks_2026(doc_id);
CREATE INDEX idx_chunks_chunk_id_2026 ON document_chunks_2026(chunk_id);

CREATE INDEX idx_graph_entity_type_2026 ON knowledge_graph_2026(entity_type);
CREATE INDEX idx_graph_relationships_2026 ON knowledge_graph_2026 USING GIN (relationships);

-- Functions

-- Update timestamp function
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger for auto-updating timestamps
CREATE TRIGGER update_docs_timestamp
BEFORE UPDATE ON legal_documents_2026
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

-- Hybrid search function (Dense + Full-text)
CREATE OR REPLACE FUNCTION hybrid_search_2026(
    query_embedding vector(1024),
    query_text TEXT,
    top_k INTEGER DEFAULT 10,
    dense_weight FLOAT DEFAULT 0.6,
    fts_weight FLOAT DEFAULT 0.4
)
RETURNS TABLE (
    doc_id VARCHAR,
    source VARCHAR,
    content TEXT,
    dense_score FLOAT,
    fts_score FLOAT,
    final_score FLOAT
) AS $$
BEGIN
    RETURN QUERY
    WITH dense_results AS (
        SELECT 
            d.doc_id,
            d.source,
            d.content,
            1 - (d.embedding <=> query_embedding) AS score
        FROM legal_documents_2026 d
        ORDER BY d.embedding <=> query_embedding
        LIMIT top_k * 2
    ),
    fts_results AS (
        SELECT 
            d.doc_id,
            d.source,
            d.content,
            ts_rank(d.content_tsvector, plainto_tsquery('english', query_text)) AS score
        FROM legal_documents_2026 d
        WHERE d.content_tsvector @@ plainto_tsquery('english', query_text)
        ORDER BY score DESC
        LIMIT top_k * 2
    ),
    combined AS (
        SELECT 
            COALESCE(d.doc_id, f.doc_id) AS doc_id,
            COALESCE(d.source, f.source) AS source,
            COALESCE(d.content, f.content) AS content,
            COALESCE(d.score, 0) AS dense_score,
            COALESCE(f.score, 0) AS fts_score,
            (COALESCE(d.score, 0) * dense_weight + COALESCE(f.score, 0) * fts_weight) AS final_score
        FROM dense_results d
        FULL OUTER JOIN fts_results f ON d.doc_id = f.doc_id
    )
    SELECT * FROM combined
    ORDER BY final_score DESC
    LIMIT top_k;
END;
$$ LANGUAGE plpgsql;

-- Sample data insertion function
CREATE OR REPLACE FUNCTION insert_sample_data_2026()
RETURNS VOID AS $$
BEGIN
    -- Insert Constitution of India sample
    INSERT INTO legal_documents_2026 (doc_id, source, title, content, doc_type, jurisdiction, year, category)
    VALUES 
    (
        'constitution_article_19',
        'Constitution of India',
        'Article 19 - Protection of certain rights regarding freedom of speech etc.',
        'Article 19. Protection of certain rights regarding freedom of speech etc.
        
        (1) All citizens shall have the right—
        (a) to freedom of speech and expression;
        (b) to assemble peaceably and without arms;
        (c) to form associations or unions;
        (d) to move freely throughout the territory of India;
        (e) to reside and settle in any part of the territory of India;
        (f) [Omitted]
        (g) to practise any profession, or to carry on any occupation, trade or business.
        
        (2) Nothing in sub-clause (a) of clause (1) shall affect the operation of any existing law, or prevent the State from making any law, in so far as such law imposes reasonable restrictions on the exercise of the right conferred by the said sub-clause in the interests of the sovereignty and integrity of India, the security of the State, friendly relations with foreign States, public order, decency or morality or in relation to contempt of court, defamation or incitement to an offence.',
        'constitution',
        'India',
        1950,
        'fundamental_rights'
    ),
    (
        'it_act_section_66a',
        'Information Technology Act, 2000 (Amended 2008)',
        'Section 66A - Punishment for sending offensive messages',
        'Section 66A. Punishment for sending offensive messages through communication service, etc.
        
        Any person who sends, by means of a computer resource or a communication device,—
        (a) any information that is grossly offensive or has menacing character; or
        (b) any information which he knows to be false, but for the purpose of causing annoyance, inconvenience, danger, obstruction, insult, injury, criminal intimidation, enmity, hatred or ill will, persistently by making use of such computer resource or a communication device; or
        (c) any electronic mail or electronic mail message for the purpose of causing annoyance or inconvenience or to deceive or to mislead the addressee or recipient about the origin of such messages,
        
        shall be punishable with imprisonment for a term which may extend to three years and with fine.
        
        [NOTE: This section was struck down by the Supreme Court in Shreya Singhal v. Union of India (2015) as unconstitutional]',
        'act',
        'India',
        2008,
        'cyber_law'
    );
    
    -- Insert knowledge graph entities
    INSERT INTO knowledge_graph_2026 (entity_id, entity_type, entity_name, relationships, source_doc_id)
    VALUES
    (
        'article_19',
        'article',
        'Article 19 - Freedom of Speech',
        '[
            {"type": "PROTECTS", "target": "freedom_of_speech", "weight": 1.0},
            {"type": "ALLOWS_RESTRICTIONS", "target": "reasonable_restrictions", "weight": 0.8},
            {"type": "RELATED_TO", "target": "article_21", "weight": 0.6}
        ]'::jsonb,
        'constitution_article_19'
    ),
    (
        'freedom_of_speech',
        'right',
        'Freedom of Speech and Expression',
        '[
            {"type": "GUARANTEED_BY", "target": "article_19", "weight": 1.0},
            {"type": "RESTRICTED_BY", "target": "section_66a", "weight": 0.7},
            {"type": "INCLUDES", "target": "internet_speech", "weight": 0.9}
        ]'::jsonb,
        'constitution_article_19'
    ),
    (
        'section_66a',
        'restriction',
        'Section 66A IT Act',
        '[
            {"type": "RESTRICTS", "target": "freedom_of_speech", "weight": 0.9},
            {"type": "STRUCK_DOWN_BY", "target": "shreya_singhal_case", "weight": 1.0}
        ]'::jsonb,
        'it_act_section_66a'
    );
    
    RAISE NOTICE 'Sample data inserted successfully';
END;
$$ LANGUAGE plpgsql;

-- Execute sample data insertion
SELECT insert_sample_data_2026();

-- Grant permissions (adjust as needed)
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO rag_user_2026;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO rag_user_2026;
