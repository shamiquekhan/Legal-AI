# evaluation.py - RAGAS & Comprehensive Evaluation Framework

"""
RAGAS: Automatic Evaluation Framework for RAG (2024)

Metrics:
- Context Relevance: Is context relevant to query?
- Faithfulness: Is answer faithful to context?
- Answer Relevance: Does answer address query?
- Answer Similarity: How similar to ground truth?

Formula:
RAG Score = 0.3×context_rel + 0.3×faithfulness + 0.2×answer_rel + 0.2×similarity
"""

from typing import List, Dict, Optional, Tuple
import numpy as np
from dataclasses import dataclass
import asyncio
from collections import defaultdict


@dataclass
class EvaluationResult:
    query: str
    answer: str
    sources: List[Dict]
    
    # RAGAS metrics
    context_relevance: float
    faithfulness: float
    answer_relevance: float
    answer_similarity: float
    ragas_score: float
    
    # Additional metrics
    ndcg_score: float
    mrr_score: float
    precision_at_5: float
    recall_at_10: float
    
    # Safety metrics
    hallucination_score: float
    citation_coverage: float
    
    # Performance
    latency_ms: float
    
    metadata: Dict


class RAGASEvaluator:
    """
    RAGAS: Retrieval-Augmented Generation Assessment
    
    Research: "RAGAS: Automated Evaluation of Retrieval Augmented Generation" (2024)
    
    Provides automatic evaluation without human annotations
    """
    
    def __init__(self, llm, embedder):
        self.llm = llm
        self.embedder = embedder
    
    async def evaluate_context_relevance(
        self,
        query: str,
        documents: List[Dict]
    ) -> float:
        """
        Context Relevance: Are retrieved documents relevant to query?
        
        Method: LLM judges relevance of each document
        Score: Average relevance across all documents
        """
        
        if not documents:
            return 0.0
        
        relevance_scores = []
        
        for doc in documents:
            prompt = f"""On a scale of 0-1, how relevant is this document to the query?

Query: {query}

Document: {doc['content'][:500]}

Relevance Score (0.0 to 1.0):"""
            
            try:
                response = await self.llm.generate(prompt, max_tokens=10)
                score = float(response.strip())
                score = max(0.0, min(1.0, score))
            except:
                score = 0.5  # Default if parsing fails
            
            relevance_scores.append(score)
        
        return np.mean(relevance_scores)
    
    async def evaluate_faithfulness(
        self,
        answer: str,
        documents: List[Dict]
    ) -> float:
        """
        Faithfulness: Is answer faithful to retrieved documents?
        
        Method:
        1. Extract claims from answer
        2. Check each claim against documents
        3. Score = supported_claims / total_claims
        """
        
        # Extract claims
        claims = await self._extract_claims(answer)
        
        if not claims:
            return 1.0  # No claims = no hallucinations
        
        # Check each claim
        supported_claims = 0
        doc_text = "\n".join([d['content'] for d in documents])
        
        for claim in claims:
            is_supported = await self._check_claim_support(claim, doc_text)
            if is_supported:
                supported_claims += 1
        
        return supported_claims / len(claims)
    
    async def evaluate_answer_relevance(
        self,
        query: str,
        answer: str
    ) -> float:
        """
        Answer Relevance: Does answer address the query?
        
        Method: Semantic similarity between query and answer
        """
        
        query_emb = await self.embedder.embed(query)
        answer_emb = await self.embedder.embed(answer)
        
        # Cosine similarity
        similarity = np.dot(query_emb, answer_emb) / (
            np.linalg.norm(query_emb) * np.linalg.norm(answer_emb)
        )
        
        return float(similarity)
    
    async def evaluate_answer_similarity(
        self,
        answer: str,
        ground_truth: str
    ) -> float:
        """
        Answer Similarity: BERTScore-based similarity to ground truth
        
        Method: Semantic similarity using embeddings
        """
        
        if not ground_truth:
            return 0.0
        
        answer_emb = await self.embedder.embed(answer)
        truth_emb = await self.embedder.embed(ground_truth)
        
        # Cosine similarity
        similarity = np.dot(answer_emb, truth_emb) / (
            np.linalg.norm(answer_emb) * np.linalg.norm(truth_emb)
        )
        
        return float(similarity)
    
    async def compute_ragas_score(
        self,
        query: str,
        answer: str,
        documents: List[Dict],
        ground_truth: Optional[str] = None
    ) -> Dict:
        """
        Compute complete RAGAS score
        
        Returns:
            {
                'context_relevance': float,
                'faithfulness': float,
                'answer_relevance': float,
                'answer_similarity': float,
                'ragas_score': float
            }
        """
        
        # Compute individual metrics
        context_rel = await self.evaluate_context_relevance(query, documents)
        faithfulness = await self.evaluate_faithfulness(answer, documents)
        answer_rel = await self.evaluate_answer_relevance(query, answer)
        
        # Answer similarity (only if ground truth available)
        if ground_truth:
            answer_sim = await self.evaluate_answer_similarity(answer, ground_truth)
        else:
            answer_sim = 0.0
        
        # RAGAS score (weighted average)
        if ground_truth:
            ragas_score = (
                0.3 * context_rel +
                0.3 * faithfulness +
                0.2 * answer_rel +
                0.2 * answer_sim
            )
        else:
            # Without ground truth, reweight
            ragas_score = (
                0.35 * context_rel +
                0.40 * faithfulness +
                0.25 * answer_rel
            )
        
        return {
            'context_relevance': context_rel,
            'faithfulness': faithfulness,
            'answer_relevance': answer_rel,
            'answer_similarity': answer_sim,
            'ragas_score': ragas_score
        }
    
    async def _extract_claims(self, answer: str) -> List[str]:
        """Extract factual claims from answer"""
        
        prompt = f"""Extract all factual claims from this answer:

Answer: {answer}

List each claim separately:"""
        
        response = await self.llm.generate(prompt, max_tokens=300)
        
        # Parse claims (assume numbered list)
        claims = []
        for line in response.split('\n'):
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('-')):
                claim = line.lstrip('0123456789.-) ')
                if claim:
                    claims.append(claim)
        
        return claims
    
    async def _check_claim_support(
        self,
        claim: str,
        document_text: str
    ) -> bool:
        """Check if claim is supported by documents"""
        
        prompt = f"""Is this claim supported by the document?

Claim: {claim}

Document: {document_text[:1000]}

Answer (Yes/No):"""
        
        response = await self.llm.generate(prompt, max_tokens=5)
        
        return 'yes' in response.lower()


class RetrievalMetrics:
    """
    Standard information retrieval metrics
    
    Metrics:
    - NDCG@k: Normalized Discounted Cumulative Gain
    - MRR@k: Mean Reciprocal Rank
    - Precision@k: Precision at k
    - Recall@k: Recall at k
    """
    
    @staticmethod
    def ndcg_at_k(relevance_scores: List[float], k: int = 10) -> float:
        """
        NDCG@k: Measures ranking quality
        
        Args:
            relevance_scores: Relevance scores in ranked order [1.0, 0.8, 0.5, ...]
            k: Top-k to consider
        
        Returns:
            NDCG score (0-1)
        """
        
        relevance_scores = relevance_scores[:k]
        
        if not relevance_scores:
            return 0.0
        
        # DCG
        dcg = relevance_scores[0]
        for i, score in enumerate(relevance_scores[1:], start=2):
            dcg += score / np.log2(i + 1)
        
        # IDCG (ideal DCG with perfect ranking)
        ideal_scores = sorted(relevance_scores, reverse=True)
        idcg = ideal_scores[0]
        for i, score in enumerate(ideal_scores[1:], start=2):
            idcg += score / np.log2(i + 1)
        
        if idcg == 0:
            return 0.0
        
        return dcg / idcg
    
    @staticmethod
    def mrr_at_k(relevance_scores: List[float], k: int = 10, threshold: float = 0.5) -> float:
        """
        MRR@k: Mean Reciprocal Rank
        
        Args:
            relevance_scores: Relevance scores in ranked order
            k: Top-k to consider
            threshold: Minimum relevance to be considered relevant
        
        Returns:
            MRR score (0-1)
        """
        
        relevance_scores = relevance_scores[:k]
        
        for i, score in enumerate(relevance_scores, start=1):
            if score >= threshold:
                return 1.0 / i
        
        return 0.0
    
    @staticmethod
    def precision_at_k(relevance_scores: List[float], k: int = 5, threshold: float = 0.5) -> float:
        """
        Precision@k: Fraction of relevant documents in top-k
        
        Args:
            relevance_scores: Relevance scores in ranked order
            k: Top-k to consider
            threshold: Minimum relevance to be considered relevant
        
        Returns:
            Precision (0-1)
        """
        
        relevance_scores = relevance_scores[:k]
        
        if not relevance_scores:
            return 0.0
        
        relevant_count = sum(1 for score in relevance_scores if score >= threshold)
        
        return relevant_count / k
    
    @staticmethod
    def recall_at_k(
        relevance_scores: List[float],
        total_relevant: int,
        k: int = 10,
        threshold: float = 0.5
    ) -> float:
        """
        Recall@k: Fraction of relevant documents retrieved
        
        Args:
            relevance_scores: Relevance scores in ranked order
            total_relevant: Total number of relevant documents in corpus
            k: Top-k to consider
            threshold: Minimum relevance to be considered relevant
        
        Returns:
            Recall (0-1)
        """
        
        relevance_scores = relevance_scores[:k]
        
        if total_relevant == 0:
            return 0.0
        
        relevant_retrieved = sum(1 for score in relevance_scores if score >= threshold)
        
        return relevant_retrieved / total_relevant


class ComprehensiveEvaluator:
    """
    Complete evaluation framework combining all metrics
    
    Evaluates:
    1. Retrieval quality (NDCG, MRR, Precision, Recall)
    2. Generation quality (RAGAS)
    3. Safety (Hallucination, Citation)
    4. Performance (Latency)
    """
    
    def __init__(self, llm, embedder):
        self.ragas = RAGASEvaluator(llm, embedder)
        self.retrieval = RetrievalMetrics()
    
    async def evaluate_complete_system(
        self,
        query: str,
        answer: str,
        documents: List[Dict],
        relevance_scores: List[float],
        total_relevant: int,
        hallucination_score: float,
        citation_count: int,
        latency_ms: float,
        ground_truth: Optional[str] = None
    ) -> EvaluationResult:
        """
        Complete system evaluation
        
        Args:
            query: User query
            answer: Generated answer
            documents: Retrieved documents
            relevance_scores: Relevance scores for each document
            total_relevant: Total relevant docs in corpus
            hallucination_score: Hallucination detection score
            citation_count: Number of citations in answer
            latency_ms: Processing time
            ground_truth: Optional ground truth answer
        
        Returns:
            EvaluationResult with all metrics
        """
        
        # RAGAS metrics
        ragas_results = await self.ragas.compute_ragas_score(
            query,
            answer,
            documents,
            ground_truth
        )
        
        # Retrieval metrics
        ndcg = self.retrieval.ndcg_at_k(relevance_scores, k=10)
        mrr = self.retrieval.mrr_at_k(relevance_scores, k=10)
        precision = self.retrieval.precision_at_k(relevance_scores, k=5)
        recall = self.retrieval.recall_at_k(relevance_scores, total_relevant, k=10)
        
        # Citation coverage
        facts_count = len(answer.split('.'))  # Rough estimate
        citation_coverage = min(1.0, citation_count / max(facts_count * 0.3, 1))
        
        return EvaluationResult(
            query=query,
            answer=answer,
            sources=documents,
            
            # RAGAS
            context_relevance=ragas_results['context_relevance'],
            faithfulness=ragas_results['faithfulness'],
            answer_relevance=ragas_results['answer_relevance'],
            answer_similarity=ragas_results['answer_similarity'],
            ragas_score=ragas_results['ragas_score'],
            
            # Retrieval
            ndcg_score=ndcg,
            mrr_score=mrr,
            precision_at_5=precision,
            recall_at_10=recall,
            
            # Safety
            hallucination_score=hallucination_score,
            citation_coverage=citation_coverage,
            
            # Performance
            latency_ms=latency_ms,
            
            metadata={
                'has_ground_truth': ground_truth is not None,
                'num_documents': len(documents),
                'num_citations': citation_count
            }
        )
    
    def compute_aggregate_metrics(
        self,
        results: List[EvaluationResult]
    ) -> Dict:
        """
        Aggregate metrics across multiple queries
        
        Returns:
            {
                'avg_ragas_score': float,
                'avg_ndcg': float,
                'avg_faithfulness': float,
                'avg_hallucination': float,
                'avg_latency_ms': float,
                'pass_rate': float  # % with ragas_score > 0.7
            }
        """
        
        if not results:
            return {}
        
        return {
            'avg_ragas_score': np.mean([r.ragas_score for r in results]),
            'avg_ndcg': np.mean([r.ndcg_score for r in results]),
            'avg_context_relevance': np.mean([r.context_relevance for r in results]),
            'avg_faithfulness': np.mean([r.faithfulness for r in results]),
            'avg_answer_relevance': np.mean([r.answer_relevance for r in results]),
            'avg_hallucination': np.mean([r.hallucination_score for r in results]),
            'avg_citation_coverage': np.mean([r.citation_coverage for r in results]),
            'avg_latency_ms': np.mean([r.latency_ms for r in results]),
            'pass_rate': sum(1 for r in results if r.ragas_score > 0.7) / len(results),
            'low_hallucination_rate': sum(1 for r in results if r.hallucination_score < 0.1) / len(results),
            'total_queries': len(results)
        }


# Example usage
async def example_evaluation():
    """Demonstrate comprehensive evaluation"""
    
    from utils.llm import get_llm_primary
    from embeddings import MixedBreadAIEmbedding
    
    llm = get_llm_primary()
    embedder = MixedBreadAIEmbedding()
    
    evaluator = ComprehensiveEvaluator(llm, embedder)
    
    # Simulate RAG output
    query = "What is Article 19?"
    answer = "Article 19 of the Constitution protects fundamental rights including freedom of speech [1]."
    documents = [
        {'content': 'Article 19 protects freedom of speech...', 'source': 'Constitution'},
        {'content': 'Related case law...', 'source': 'Judgment'}
    ]
    relevance_scores = [0.95, 0.75]
    
    result = await evaluator.evaluate_complete_system(
        query=query,
        answer=answer,
        documents=documents,
        relevance_scores=relevance_scores,
        total_relevant=5,
        hallucination_score=0.02,
        citation_count=1,
        latency_ms=1850
    )
    
    print(f"RAGAS Score: {result.ragas_score:.3f}")
    print(f"NDCG@10: {result.ndcg_score:.3f}")
    print(f"Faithfulness: {result.faithfulness:.3f}")
    print(f"Hallucination: {result.hallucination_score:.3f}")


if __name__ == "__main__":
    asyncio.run(example_evaluation())
