# query_expansion.py - Advanced Query Expansion with HyDE

"""
HyDE: Hypothetical Document Embeddings (2024)

Key Insight: Query better understood through hypothetical documents

Method:
1. Generate 3-5 hypothetical documents for query
2. Embed these documents
3. Average embeddings for better query representation
4. Retrieve using averaged embedding

Result: 10-15% improvement in retrieval quality
"""

from typing import List, Dict, Optional
import numpy as np
from dataclasses import dataclass


@dataclass
class ExpandedQuery:
    original_query: str
    hypothetical_docs: List[str]
    averaged_embedding: np.ndarray
    expansion_method: str
    metadata: Dict


class HyDEQueryExpander:
    """
    Hypothetical Document Embeddings for query expansion
    
    Research: "Precise Zero-Shot Dense Retrieval without Relevance Labels" (2024)
    
    Key Innovation: Generate hypothetical answer, then search for it
    Better than searching for question directly
    """
    
    def __init__(self, llm, embedder):
        self.llm = llm
        self.embedder = embedder
    
    async def expand_query_with_hyde(
        self,
        query: str,
        num_hypothetical: int = 3
    ) -> ExpandedQuery:
        """
        Generate hypothetical documents and average embeddings
        
        Args:
            query: User's legal query
            num_hypothetical: Number of hypothetical docs (default: 3)
        
        Returns:
            ExpandedQuery with averaged embedding
        """
        
        # Step 1: Generate hypothetical documents
        hypothetical_docs = await self._generate_hypothetical_documents(
            query,
            num_hypothetical
        )
        
        # Step 2: Embed all hypothetical documents
        embeddings = []
        for doc in hypothetical_docs:
            emb = await self.embedder.embed(doc)
            embeddings.append(emb)
        
        # Step 3: Average embeddings
        averaged_embedding = np.mean(embeddings, axis=0)
        
        # Normalize (important for cosine similarity)
        averaged_embedding = averaged_embedding / np.linalg.norm(averaged_embedding)
        
        return ExpandedQuery(
            original_query=query,
            hypothetical_docs=hypothetical_docs,
            averaged_embedding=averaged_embedding,
            expansion_method='hyde',
            metadata={
                'num_hypothetical': num_hypothetical,
                'embedding_dim': len(averaged_embedding)
            }
        )
    
    async def _generate_hypothetical_documents(
        self,
        query: str,
        num_docs: int
    ) -> List[str]:
        """
        Generate hypothetical legal documents that would answer the query
        
        Technique: Ask LLM to write hypothetical judgment/statute excerpt
        """
        
        hypothetical_docs = []
        
        # Generate diverse hypothetical documents
        for i in range(num_docs):
            if i == 0:
                # First: Straightforward answer
                prompt = f"""Write a brief legal document excerpt that answers this query:

Query: {query}

Write as if this is from a legal judgment or statute. Be specific and factual.

Hypothetical Document:"""
            
            elif i == 1:
                # Second: Constitutional perspective
                prompt = f"""Write a brief constitutional law excerpt addressing:

Query: {query}

Focus on fundamental rights and constitutional principles.

Hypothetical Document:"""
            
            else:
                # Third: Case law perspective
                prompt = f"""Write a brief Supreme Court judgment excerpt deciding:

Query: {query}

Include reasoning and legal precedent.

Hypothetical Document:"""
            
            doc = await self.llm.generate(prompt, max_tokens=300)
            hypothetical_docs.append(doc.strip())
        
        return hypothetical_docs


class MultiQueryExpander:
    """
    Generate multiple query variations for better coverage
    
    Technique: Rephrase query in different ways, retrieve for each, merge results
    """
    
    def __init__(self, llm):
        self.llm = llm
    
    async def generate_query_variations(
        self,
        query: str,
        num_variations: int = 3
    ) -> List[str]:
        """
        Generate multiple rephrased versions of the query
        
        Example:
            Original: "What is Section 302?"
            Variations:
            - "Explain Section 302 of IPC"
            - "What does Section 302 Indian Penal Code say?"
            - "Section 302 punishment for murder details"
        """
        
        prompt = f"""Rephrase this legal query in {num_variations} different ways:

Original Query: {query}

Guidelines:
- Keep the same legal intent
- Use different terminology/phrasing
- Include synonyms and legal terms
- Make questions more specific

Variations:"""
        
        response = await self.llm.generate(prompt, max_tokens=200)
        
        # Parse variations (assume numbered list)
        variations = []
        for line in response.split('\n'):
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('-')):
                # Remove numbering
                cleaned = line.lstrip('0123456789.-) ')
                if cleaned:
                    variations.append(cleaned)
        
        # Always include original
        variations.insert(0, query)
        
        return variations[:num_variations + 1]


class MetadataExtractor:
    """
    Extract metadata filters from natural language query
    
    Example:
        Query: "Recent Supreme Court cases on Article 19 after 2020"
        Metadata: {
            'court': 'Supreme Court',
            'article': '19',
            'year_start': 2020,
            'year_end': 2026
        }
    """
    
    def __init__(self, llm):
        self.llm = llm
    
    async def extract_filters(self, query: str) -> Dict:
        """
        Extract structured filters from natural language query
        
        Filters:
        - court: Supreme Court, High Court, District Court
        - section: Section number (e.g., "302", "66A")
        - article: Article number (e.g., "19", "21")
        - year_range: (start, end)
        - doc_type: judgment, statute, constitution
        - jurisdiction: India, specific state
        """
        
        prompt = f"""Extract structured legal filters from this query:

Query: {query}

Extract (return "null" if not mentioned):
- Court: (Supreme Court / High Court / District Court)
- Section: (e.g., "302", "66A")
- Article: (e.g., "19", "21")
- Year Start: (earliest year mentioned)
- Year End: (latest year mentioned, or 2026 for "recent")
- Doc Type: (judgment / statute / constitution)
- Jurisdiction: (India / specific state)

Output JSON:"""
        
        response = await self.llm.generate(prompt, max_tokens=200)
        
        # Parse JSON response
        try:
            import json
            filters = json.loads(response)
        except:
            # Fallback to manual parsing
            filters = self._manual_parse(query)
        
        # Clean up nulls
        filters = {k: v for k, v in filters.items() if v and v != "null"}
        
        return filters
    
    def _manual_parse(self, query: str) -> Dict:
        """Fallback manual parsing using regex"""
        import re
        
        filters = {}
        
        # Court extraction
        if 'supreme court' in query.lower():
            filters['court'] = 'Supreme Court'
        elif 'high court' in query.lower():
            filters['court'] = 'High Court'
        
        # Section extraction (e.g., "Section 302", "Section 66A")
        section_match = re.search(r'section\s+(\d+[A-Z]*)', query, re.IGNORECASE)
        if section_match:
            filters['section'] = section_match.group(1)
        
        # Article extraction (e.g., "Article 19", "Article 21")
        article_match = re.search(r'article\s+(\d+)', query, re.IGNORECASE)
        if article_match:
            filters['article'] = article_match.group(1)
        
        # Year extraction
        years = re.findall(r'\b(19|20)\d{2}\b', query)
        if years:
            years = [int(y) for y in years]
            filters['year_start'] = min(years)
            filters['year_end'] = max(years)
        
        # "Recent" keyword
        if 'recent' in query.lower():
            filters['year_start'] = 2020
            filters['year_end'] = 2026
        
        return filters


class AdvancedQueryProcessor:
    """
    Complete query processing pipeline combining all techniques
    
    Pipeline:
    1. Extract metadata filters
    2. Generate query variations
    3. Apply HyDE expansion
    4. Return processed query ready for retrieval
    """
    
    def __init__(self, llm, embedder):
        self.llm = llm
        self.embedder = embedder
        
        self.hyde_expander = HyDEQueryExpander(llm, embedder)
        self.multi_query = MultiQueryExpander(llm)
        self.metadata_extractor = MetadataExtractor(llm)
    
    async def process_query(
        self,
        query: str,
        use_hyde: bool = True,
        use_variations: bool = False,
        extract_metadata: bool = True
    ) -> Dict:
        """
        Complete query processing
        
        Returns:
            {
                'original_query': str,
                'processed_query': str,
                'embedding': np.ndarray,
                'variations': List[str],
                'filters': Dict,
                'hypothetical_docs': List[str],
                'method': str
            }
        """
        
        result = {
            'original_query': query,
            'processed_query': query,
            'variations': [query],
            'filters': {},
            'hypothetical_docs': [],
            'method': 'standard'
        }
        
        # Step 1: Extract metadata filters
        if extract_metadata:
            filters = await self.metadata_extractor.extract_filters(query)
            result['filters'] = filters
        
        # Step 2: HyDE expansion
        if use_hyde:
            expanded = await self.hyde_expander.expand_query_with_hyde(query)
            result['embedding'] = expanded.averaged_embedding
            result['hypothetical_docs'] = expanded.hypothetical_docs
            result['method'] = 'hyde'
        else:
            # Standard embedding
            result['embedding'] = await self.embedder.embed(query)
            result['method'] = 'standard'
        
        # Step 3: Query variations (optional)
        if use_variations:
            variations = await self.multi_query.generate_query_variations(query)
            result['variations'] = variations
            result['method'] = 'hyde+variations' if use_hyde else 'variations'
        
        return result


# Example usage
async def example_usage():
    """
    Demonstrates advanced query expansion
    """
    
    from utils.llm import get_llm_primary
    from embeddings import MixedBreadAIEmbedding
    
    llm = get_llm_primary()
    embedder = MixedBreadAIEmbedding()
    
    processor = AdvancedQueryProcessor(llm, embedder)
    
    # Process query with all enhancements
    query = "Recent Supreme Court cases on Article 19 freedom of speech after 2020"
    
    processed = await processor.process_query(
        query,
        use_hyde=True,
        use_variations=True,
        extract_metadata=True
    )
    
    print(f"Original: {processed['original_query']}")
    print(f"Method: {processed['method']}")
    print(f"Filters: {processed['filters']}")
    print(f"Variations: {len(processed['variations'])}")
    print(f"Hypothetical Docs: {len(processed['hypothetical_docs'])}")
    print(f"Embedding shape: {processed['embedding'].shape}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(example_usage())
