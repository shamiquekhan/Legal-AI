"""
Legal AI RAG - Production Grade System

A state-of-the-art RAG system for legal queries combining:
- Hybrid retrieval (dense + sparse + semantic)
- Educational intent analysis
- Legal knowledge base with IPC punishments
- Safety and hallucination detection
"""

__version__ = "1.0.0"
__author__ = "Legal AI Team"

# Core modules
from .intent_analyzer import EducationalIntentAnalyzer
from .legal_knowledge import format_punishment_answer

__all__ = [
    "EducationalIntentAnalyzer",
    "format_punishment_answer"
]
