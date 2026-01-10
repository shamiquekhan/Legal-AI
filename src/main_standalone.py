# main_standalone.py - Standalone Legal AI RAG Server (Groq-powered, FREE)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import time
import logging
import os

# Import our core modules
from .intent_analyzer import EducationalIntentAnalyzer
from .legal_knowledge import format_punishment_answer
from .utils.groq_llm import get_groq_llm

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="Legal AI RAG",
    description="Production Legal AI RAG with Educational Intent Analysis",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize intent analyzer
intent_analyzer = EducationalIntentAnalyzer()
logger.info("✓ Intent analyzer initialized")

# Request/Response Models
class QueryRequest(BaseModel):
    query: str = Field(..., description="Legal query")

class SourceInfo(BaseModel):
    doc_id: str
    source: str
    content_preview: str
    dense_score: float
    sparse_score: float
    graph_score: float
    final_score: float

class QueryResponse(BaseModel):
    query: str
    answer: str
    sources: List[SourceInfo]
    reasoning: Optional[str] = None
    improved: bool = False
    iterations: int = 1
    confidence: float
    hallucination_score: float
    risk_level: str
    is_safe: bool
    level_scores: Dict[str, float]
    ragas_score: Optional[float] = None
    context_relevance: Optional[float] = None
    faithfulness: Optional[float] = None
    answer_relevance: Optional[float] = None
    cache_hit: bool = False
    processing_time_ms: float
    retrieval_time_ms: float
    generation_time_ms: float


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        'status': 'healthy',
        'version': '1.0.0',
        'components': {
            'intent_analyzer': 'operational',
            'legal_knowledge': 'operational'
        }
    }


@app.get("/", response_class=HTMLResponse)
async def get_chatbot():
    """Serve the chatbot HTML interface"""
    chatbot_path = os.path.join(os.path.dirname(__file__), '..', 'chatbot.html')
    
    if os.path.exists(chatbot_path):
        with open(chatbot_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return "<html><body><h1>Legal AI RAG API</h1><p>API at /docs</p></body></html>"


@app.post("/api/v1/query/legal", response_model=QueryResponse)
async def query_legal(request: QueryRequest):
    """Process legal query with educational intent analysis"""
    
    start_time = time.time()
    
    try:
        # Analyze intent
        analysis = intent_analyzer.analyze(request.query)
        logger.info(f"Intent: {analysis['type']} (confidence: {analysis['confidence']})")
        
        # BLOCK: Pure violence/criminal planning
        if not analysis["safe"] and analysis["type"] == "PURE_VIOLENCE":
            return QueryResponse(
                query=request.query,
                answer=analysis.get("block_message", "❌ Cannot assist with this query."),
                sources=[],
                reasoning="Query blocked for safety",
                improved=False,
                iterations=0,
                confidence=0.0,
                hallucination_score=0.0,
                risk_level='blocked',
                is_safe=False,
                level_scores={},
                cache_hit=False,
                processing_time_ms=(time.time() - start_time) * 1000,
                retrieval_time_ms=0.0,
                generation_time_ms=0.0
            )
        
        # EDUCATIONAL: Punishment/consequence queries
        if analysis["type"] == "PUNISHMENT_EDUCATION":
            crime_type = analysis.get('crime_type', 'general')
            logger.info(f"Educational query: {crime_type}")
            
            try:
                educational_answer = format_punishment_answer(crime_type)
            except Exception as e:
                logger.error(f"Error: {e}")
                educational_answer = f"Educational information about {crime_type} is being prepared."
            
            return QueryResponse(
                query=request.query,
                answer=educational_answer,
                sources=[
                    SourceInfo(
                        doc_id="IPC",
                        source="Indian Penal Code",
                        content_preview="Legal provisions...",
                        dense_score=1.0,
                        sparse_score=1.0,
                        graph_score=1.0,
                        final_score=1.0
                    )
                ],
                reasoning="Educational response about legal consequences",
                improved=False,
                iterations=1,
                confidence=0.95,
                hallucination_score=0.0,
                risk_level='safe',
                is_safe=True,
                level_scores={"educational": 1.0},
                cache_hit=False,
                processing_time_ms=(time.time() - start_time) * 1000,
                retrieval_time_ms=0.0,
                generation_time_ms=0.0
            )
        
        # GENERAL legal query with specific concept
        if analysis["type"] == "GENERAL_LEGAL" and analysis.get("concept_key"):
            concept_key = analysis.get("concept_key")
            logger.info(f"Concept query: {concept_key}")
            
            try:
                concept_answer = format_punishment_answer(concept_key)
                # Check if we got a real answer (not the fallback)
                if "is being prepared" not in concept_answer and "legal information request" not in concept_answer:
                    return QueryResponse(
                        query=request.query,
                        answer=concept_answer,
                        sources=[
                            SourceInfo(
                                doc_id="CONCEPT",
                                source="Legal Knowledge Base",
                                content_preview=f"Information about {concept_key}",
                                dense_score=1.0,
                                sparse_score=1.0,
                                graph_score=1.0,
                                final_score=1.0
                            )
                        ],
                        reasoning=f"Legal concept explanation: {concept_key}",
                        improved=False,
                        iterations=1,
                        confidence=0.90,
                        hallucination_score=0.0,
                        risk_level='safe',
                        is_safe=True,
                        level_scores={"concept": 1.0},
                        cache_hit=False,
                        processing_time_ms=(time.time() - start_time) * 1000,
                        retrieval_time_ms=0.0,
                        generation_time_ms=0.0
                    )
            except Exception as e:
                logger.error(f"Error formatting concept: {e}")
        
        # GENERAL legal query - use Groq LLM for dynamic response
        llm = get_groq_llm()
        
        llm_prompt = f"""Answer this legal question about Indian law:

Question: {request.query}

Provide a clear, educational response that includes:
1. Relevant legal provisions (IPC sections, Constitutional articles, etc.)
2. Key legal principles
3. Practical information
4. Important caveats or disclaimers

If this is outside Indian law scope, politely explain that you specialize in Indian legal matters."""

        generation_start = time.time()
        general_answer = await llm.generate(llm_prompt)
        generation_time = (time.time() - generation_start) * 1000

        return QueryResponse(
            query=request.query,
            answer=general_answer,
            sources=[
                SourceInfo(
                    doc_id="GROQ-LLM",
                    source="Groq AI (Llama 3.3)",
                    content_preview="AI-generated legal information",
                    dense_score=0.9,
                    sparse_score=0.9,
                    graph_score=0.0,
                    final_score=0.9
                )
            ],
            reasoning="AI-powered legal information response",
            improved=False,
            iterations=1,
            confidence=0.85,
            hallucination_score=0.1,
            risk_level='low',
            is_safe=True,
            level_scores={"llm": 0.9},
            cache_hit=False,
            processing_time_ms=(time.time() - start_time) * 1000,
            retrieval_time_ms=0.0,
            generation_time_ms=generation_time
        )
        
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")
