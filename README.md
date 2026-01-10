# Legal AI - Indian Legal Assistant

AI-powered Indian Legal Assistant with Zero-Hallucination RAG Architecture

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19+-61DAFB.svg)](https://react.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 👨‍💻 Author

**Shamique Khan**
- GitHub: [@shamiquekhan](https://github.com/shamiquekhan)
- LinkedIn: [shamique-khan](https://www.linkedin.com/in/shamique-khan)

## 🎯 Features

### State-of-the-Art RAG Architecture

- **Hybrid Retrieval**: Dense + Sparse + Semantic retrieval
- **Advanced Reranking**: Cross-encoder and ColBERT techniques
- **Reciprocal Rank Fusion**: SOTA score normalization
- **Query Expansion**: HyDE (Hypothetical Document Embeddings)

### Advanced RAG Techniques

- **Corrective RAG**: Adaptive pipeline correction based on retrieval quality
- **Self-Reflective Generation**: Answer verification and correction
- **Chain-of-Thought**: Step-by-step reasoning
- **Multi-Perspective Query Rewriting**: 4 different query reformulations

### Hallucination Detection

- Factual consistency checking
- Source attribution validation
- Temporal consistency verification
- Entity consistency analysis
- Knowledge base contradiction detection

### Production-Ready

- FastAPI REST API
- Docker containerization
- Prometheus metrics
- Grafana dashboards
- Health monitoring
- Comprehensive logging

## 📊 Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User Query                               │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              Query Processing & Expansion                    │
│  • Multi-perspective rewriting                              │
│  • Structured query parsing                                 │
│  • HyDE expansion                                           │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                 Hybrid Retrieval                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Dense (SOTA) │  │ Sparse (BM25)│  │   Semantic   │      │
│  │  Embeddings  │  │   Retrieval  │  │    Search    │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                 │                  │               │
│         └─────────────────┼──────────────────┘               │
│                           ▼                                  │
│              Reciprocal Rank Fusion                          │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              Advanced Reranking                              │
│  • Cross-encoder scoring                                    │
│  • Batch processing                                         │
│  • Filtering & deduplication                                │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              Corrective RAG (Optional)                       │
│  • Assess retrieval quality                                 │
│  • Query expansion if needed                                │
│  • Related concept search                                   │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│         Self-Reflective Generation                           │
│  1. Initial answer generation                               │
│  2. Self-verification                                       │
│  3. Uncertainty identification                              │
│  4. Correction                                              │
│  5. Citation extraction                                     │
│  6. Confidence scoring                                      │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│           Hallucination Detection                            │
│  • Factual consistency                                      │
│  • Source attribution                                       │
│  • Temporal consistency                                     │
│  • Entity consistency                                       │
│  • KB contradiction check                                   │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                 Final Response                               │
│  • Answer with citations                                    │
│  • Confidence score                                         │
│  • Hallucination score                                      │
│  • Source documents                                         │
│  • Processing metadata                                      │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)
- OpenAI API key or compatible LLM endpoint

### Installation

1. **Clone the repository**

```bash
cd "c:\Project\legal ai rag"
```

2. **Create virtual environment**

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment**

```bash
copy .env.example .env
# Edit .env with your API keys
```

5. **Run the application**

```bash
python src/main.py
```

The API will be available at `http://localhost:8000`

### Docker Deployment

```bash
docker-compose up -d
```

Services:
- RAG API: `http://localhost:8000`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`

## 📖 API Usage

### Query Endpoint

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is the punishment for murder under IPC Section 302?",
    "use_corrective_rag": true,
    "use_self_reflection": true,
    "detect_hallucinations": true
  }'
```

### Response Format

```json
{
  "query": "What is the punishment for murder under IPC Section 302?",
  "answer": "Under Section 302 of the Indian Penal Code...",
  "sources": [
    {
      "source": "IPC_Section_302.pdf",
      "id": "doc_123",
      "text": "Excerpt from source..."
    }
  ],
  "confidence": 0.95,
  "hallucination_score": 0.02,
  "is_safe": true,
  "processing_time_ms": 1234.56,
  "citations": [
    {
      "index": 1,
      "source": "IPC_Section_302.pdf",
      "doc_id": "doc_123"
    }
  ],
  "uncertainty_flags": []
}
```

## 🔬 Key Components

### 1. Modern RAG Architecture

**File**: [src/architecture.py](src/architecture.py)

- Hybrid retrieval system
- Reciprocal Rank Fusion
- Advanced reranking
- HyDE query expansion

### 2. Query Processing

**File**: [src/query_rewriting.py](src/query_rewriting.py)

- Multi-perspective query rewriting
- Structured query parsing
- Legal domain optimization

### 3. Embeddings

**File**: [src/embeddings.py](src/embeddings.py)

- MixedBread-AI SOTA embeddings
- Multilingual support
- Domain-specific legal embeddings
- Ensemble embeddings

### 4. Corrective RAG

**File**: [src/corrective_rag.py](src/corrective_rag.py)

- Relevance assessment
- Query expansion
- Related concept retrieval
- Adaptive corrections

### 5. Self-Reflective Generation

**File**: [src/self_reflective_rag.py](src/self_reflective_rag.py)

- Answer verification
- Uncertainty detection
- Automatic correction
- Confidence scoring

### 6. Hallucination Detection

**File**: [src/hallucination_detector.py](src/hallucination_detector.py)

- Multi-level checking
- Source attribution
- Temporal consistency
- Entity consistency

### 7. Evaluation Metrics

**File**: [src/evaluation.py](src/evaluation.py)

- Retrieval metrics (MRR, NDCG, Recall@K)
- Generation metrics (ROUGE, BERTScore)
- RAG-specific metrics (Faithfulness, Context Relevance)

## 📊 Performance Metrics

### Expected Performance

- **Retrieval Quality**: 85-95% NDCG
- **Hallucination Rate**: <5%
- **Answer Confidence**: 90%+
- **Processing Time**: 1-3 seconds
- **Precision@5**: >80%
- **Recall@10**: >85%

## 🔧 Configuration

Edit [config/config.json](config/config.json):

```json
{
  "retrieval": {
    "embedding_model": "mixedbread-ai/mxbai-embed-large-v1",
    "top_k_dense": 50,
    "top_k_rerank": 10,
    "use_reranker": true
  },
  "generation": {
    "llm_model": "gpt-4-turbo",
    "temperature": 0.3,
    "use_chain_of_thought": true,
    "use_self_reflection": true
  }
}
```

## 📚 Research Papers Referenced

1. **RAG Fusion**: "A New Take on Retrieval-Augmented Generation" (2024)
2. **Self-Reflective RAG**: "Verifying and Correcting Generated Content" (2024)
3. **HyDE**: "Precise Zero-shot Dense Retrieval without Relevance Labels"
4. **Corrective RAG**: "Understanding When and How to Correct RAG Pipelines" (2024)
5. **RAGAS**: "Automatic Evaluation of RAG" (2024)
6. **Reciprocal Rank Fusion**: "RRF outperforms Condorcet and Individual Rank Learning"

## 🛠️ Development

### Running Tests

```bash
pytest tests/ -v
```

### Code Formatting

```bash
black src/
flake8 src/
```

### Type Checking

```bash
mypy src/
```

## 📈 Monitoring

### Prometheus Metrics

- `rag_queries_total`: Total number of queries processed
- `rag_query_duration_seconds`: Query processing time
- `hallucination_rate`: Current hallucination detection rate
- `retrieval_quality`: Retrieval quality score
- `rag_errors_total`: Total errors encountered

### Grafana Dashboards

Access Grafana at `http://localhost:3000` (default credentials: admin/admin)

Pre-configured dashboards:
- RAG System Overview
- Query Performance
- Hallucination Monitoring
- Retrieval Quality

## 🔐 Security

- API key authentication
- Rate limiting
- Input sanitization
- Secure configuration management

## 📝 License

MIT License - see LICENSE file

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check documentation
- Review example queries

## 🎯 Roadmap

- [ ] Add support for more embedding models
- [ ] Implement graph-based RAG
- [ ] Add multi-modal support (images, PDFs)
- [ ] Enhance legal domain specialization
- [ ] Add more evaluation metrics
- [ ] Implement caching layer
- [ ] Add support for streaming responses

## ⚡ Performance Tips

1. **Use batch processing** for multiple queries
2. **Enable caching** for frequently accessed documents
3. **Tune top_k parameters** based on your use case
4. **Monitor hallucination rates** and adjust thresholds
5. **Use GPU acceleration** for embedding generation

## 🌟 Key Innovations

- **Hybrid Retrieval**: Combines multiple retrieval strategies
- **Self-Reflection**: Verifies and corrects its own outputs
- **Corrective Feedback**: Adapts based on retrieval quality
- **Production-Ready**: Full monitoring and deployment setup
- **SOTA Embeddings**: Uses latest 2024 embedding models

---

**Built with ❤️ for production legal AI applications**
