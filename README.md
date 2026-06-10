# ⚖️ Legal AI - Advanced Indian Legal Assistant

**Indian Legal Assistant with Zero-Hallucination RAG Architecture & Constitutional Verification**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19+-61DAFB.svg)](https://react.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 👨‍💻 Author

**Shamique Khan**
- GitHub: [@shamiquekhan](https://github.com/shamiquekhan)
- LinkedIn: [shamique-khan](https://www.linkedin.com/in/shamique-khan)

---

## 🎯 Project Overview

This project represents the ultimate fusion of **Legal AI** (Robust RAG Architecture) and **Constitutional AI** (Verification & Compliance). It provides a production-ready, zero-hallucination legal research assistant tailored for the Indian legal system.

### **Key Innovations**
- **Hybrid Retrieval System:** Combines Dense (SOTA Embeddings), Sparse (BM25), and Semantic search.
- **Constitutional Verification Layer:** Multi-step check for citation existence, accuracy, status, and jurisdiction.
- **Self-Reflective RAG:** Automatically identifies and corrects its own uncertainties.
- **Scandinavian Design UI:** Modern, clean, and intuitive legal research interface.

---

## 🌟 Advanced Features

### 1. State-of-the-Art RAG Architecture
- **Corrective RAG:** Adaptive pipeline correction based on retrieval quality.
- **Query Expansion:** HyDE (Hypothetical Document Embeddings) and multi-perspective rewriting.
- **Advanced Reranking:** Cross-encoder and ColBERT techniques for precision.

### 2. Hallucination Prevention & Verification
- **Factual Consistency Checking:** Cross-references generation against source documents.
- **Citation Verification:** Checks if cited sections are active, amended, or repealed.
- **Entity & Temporal Consistency:** Ensures people, dates, and sequences remain accurate.

### 3. Legal Specialization
- **HOMO-LUMO Spectroscopy Analysis** (Integrated from Quantum Project for molecular-legal crossover research)
- **Indian Penal Code (IPC) & Constitution Deep Integration**
- **Memorandum Generator:** Automatically creates structured legal memos.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User Query                               │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              Query Processing & Expansion                    │
│  • Multi-perspective rewriting | HyDE expansion              │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                 Hybrid Retrieval (Vector + BM25)             │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              Advanced Reranking & Filtering                  │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│         Generation with Constitutional Verification         │
│  1. Self-Reflective Generation                              │
│  2. Citation Status & Accuracy Check                        │
│  3. Confidence Scoring                                      │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                 Final Grounded Response                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation & Setup

### **Prerequisites**
- Python 3.11+
- Node.js (for Frontend)
- OpenAI API Key (or equivalent)
- Pinecone/Elasticsearch (Optional, for advanced scaling)

### **Quick Start**

1. **Clone & Install Backend**
```bash
git clone https://github.com/shamiquekhan/Legal-AI.git
cd Legal-AI
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

2. **Install Frontend**
```bash
cd frontend
npm install
npm run dev
```

---

## 📂 Project Structure

```
.
├── src/                # Core RAG logic, generation, and safety
├── backend/            # API endpoints and service layers (Constitutional)
├── frontend/           # React + TypeScript Scandinavian UI
├── database/           # Vector store and metadata management
├── config/             # System and model configurations
├── docs/               # Advanced RAG guides and architecture diagrams
├── requirements.txt    # Unified dependency list
└── README.md           # This file
```

---

## 📄 License & Credits

This project is licensed under the MIT License.

**Developed by Shamique Khan**
Special thanks to the open-source legal AI community.
