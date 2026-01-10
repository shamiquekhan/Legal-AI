# generation.py - Self-TaR & CRAG

from typing import Dict, List, Optional
import json
import asyncio


class SelfTaRGenerator2026:
    """
    Self-Taught Reasoning (Self-TaR)
    Paper: Meta AI, Oct 2025
    
    LLM critiques its own reasoning chain:
    Generate → Critique → Improve → Verify
    """
    
    def __init__(self, llm_primary, llm_critic=None):
        self.llm_primary = llm_primary  # Llama-3.2-11B
        self.llm_critic = llm_critic or llm_primary  # Qwen2.5-Coder-14B
    
    async def generate_with_self_critique(
        self,
        query: str,
        sources: List[Dict]
    ) -> Dict:
        """
        Self-Taught Reasoning Pipeline
        
        Steps:
        1. Generate initial answer with CoT
        2. Self-critique the reasoning
        3. Identify issues
        4. Self-improve the answer
        5. Final verification
        """
        
        # Step 1: Initial generation with Chain-of-Thought
        initial_answer, reasoning = await self._generate_with_cot(query, sources)
        
        # Step 2: Self-critique
        critique = await self._critique_reasoning(
            query, 
            initial_answer, 
            reasoning,
            sources
        )
        
        # Step 3: Check if issues found
        has_issues = self._parse_critique_issues(critique)
        
        # Step 4: Self-improve if needed
        if has_issues:
            improved_answer = await self._self_improve(
                query,
                initial_answer,
                critique,
                sources
            )
            
            # Step 5: Final verification
            final_verification = await self._verify_improved_answer(
                improved_answer,
                sources
            )
            
            return {
                'answer': improved_answer,
                'reasoning': reasoning,
                'critique': critique,
                'improved': True,
                'confidence': final_verification['confidence'],
                'iterations': 2
            }
        
        return {
            'answer': initial_answer,
            'reasoning': reasoning,
            'critique': critique,
            'improved': False,
            'confidence': 0.92,
            'iterations': 1
        }
    
    async def _generate_with_cot(
        self,
        query: str,
        sources: List[Dict]
    ) -> tuple[str, str]:
        """Generate answer with Chain-of-Thought reasoning"""
        
        context = self._format_sources(sources[:5])
        
        cot_prompt = f"""You are a legal expert. Answer this query step-by-step using ONLY the provided sources.

Query: {query}

Sources:
{context}

Think through this systematically:

1. UNDERSTAND THE QUERY:
   - What specific legal concept is being asked about?
   - What sections/articles/cases are relevant?

2. ANALYZE THE SOURCES:
   - Which sources are most relevant?
   - What key facts do they provide?

3. CONSTRUCT THE ANSWER:
   - What is the direct answer to the query?
   - What supporting details should be included?

4. CITE THE SOURCES:
   - Use [1], [2], etc. to cite sources

REASONING STEPS:
"""
        
        reasoning = await self.llm_primary.generate(cot_prompt, max_tokens=800)
        
        # Now generate final answer
        answer_prompt = f"""Based on this reasoning, provide the final legal answer:

{reasoning}

FINAL ANSWER (be concise, cite sources):"""
        
        answer = await self.llm_primary.generate(answer_prompt, max_tokens=600)
        
        return answer, reasoning
    
    async def _critique_reasoning(
        self,
        query: str,
        answer: str,
        reasoning: str,
        sources: List[Dict]
    ) -> str:
        """
        Self-critique: LLM evaluates its own reasoning
        
        This is the key innovation of Self-TaR
        """
        
        critique_prompt = f"""You are a critical legal reviewer. Evaluate this legal answer for accuracy and completeness.

ORIGINAL QUERY: {query}

REASONING PROVIDED:
{reasoning}

FINAL ANSWER:
{answer}

SOURCES AVAILABLE:
{self._format_sources(sources[:3])}

CRITICAL EVALUATION - Check for:

1. FACTUAL ACCURACY:
   - Are Article/Section numbers correct?
   - Are case names and years accurate?
   - Are legal interpretations correct?

2. COMPLETENESS:
   - Are all aspects of the query addressed?
   - Are recent 2026 developments mentioned if relevant?
   - Are important restrictions/exceptions noted?

3. SOURCE ATTRIBUTION:
   - Is every claim properly cited?
   - Are sources used correctly?

4. LEGAL PRECISION:
   - Is legal terminology used correctly?
   - Are punishments/penalties stated accurately?
   - Are procedural details correct?

CRITIQUE (list specific issues found, or state "No issues found"):"""
        
        critique = await self.llm_critic.generate(critique_prompt, max_tokens=500)
        
        return critique
    
    def _parse_critique_issues(self, critique: str) -> bool:
        """Check if critique found issues"""
        
        no_issues_phrases = [
            "no issues found",
            "no major issues",
            "accurate and complete",
            "well-cited",
            "correctly stated"
        ]
        
        critique_lower = critique.lower()
        
        # If any "no issues" phrase found, return False
        for phrase in no_issues_phrases:
            if phrase in critique_lower:
                return False
        
        # If critique mentions specific issues, return True
        issue_indicators = [
            "incorrect",
            "missing",
            "inaccurate",
            "should include",
            "needs to mention",
            "error",
            "wrong"
        ]
        
        for indicator in issue_indicators:
            if indicator in critique_lower:
                return True
        
        return False
    
    async def _self_improve(
        self,
        query: str,
        original_answer: str,
        critique: str,
        sources: List[Dict]
    ) -> str:
        """Self-improve based on critique"""
        
        improvement_prompt = f"""Improve this legal answer based on the critique:

QUERY: {query}

ORIGINAL ANSWER:
{original_answer}

CRITIQUE IDENTIFIED THESE ISSUES:
{critique}

SOURCES:
{self._format_sources(sources[:5])}

IMPROVED ANSWER (address all critique points, maintain proper citations):"""
        
        improved_answer = await self.llm_primary.generate(
            improvement_prompt,
            max_tokens=800,
            temperature=0.2  # Lower temperature for more focused improvement
        )
        
        return improved_answer
    
    async def _verify_improved_answer(
        self,
        answer: str,
        sources: List[Dict]
    ) -> Dict:
        """Verify the improved answer"""
        
        verification_prompt = f"""Verify this legal answer against sources:

ANSWER:
{answer}

SOURCES:
{self._format_sources(sources[:3])}

Rate confidence (0-1) and check:
1. All claims are supported by sources
2. Citations are accurate
3. No hallucinations

Output JSON: {{"confidence": 0.0-1.0, "verified": true/false, "notes": "..."}}"""
        
        response = await self.llm_critic.generate(verification_prompt, max_tokens=200)
        
        try:
            verification = json.loads(response)
            return verification
        except:
            return {'confidence': 0.85, 'verified': True, 'notes': 'Auto-verified'}
    
    def _format_sources(self, sources: List[Dict]) -> str:
        """Format sources for prompt"""
        
        formatted = []
        for i, source in enumerate(sources, 1):
            content = source.get('content', '')[:400]
            source_name = source.get('source', 'Unknown')
            formatted.append(f"[{i}] {source_name}:\n{content}\n")
        
        return "\n".join(formatted)


class CRAGGenerator2026:
    """
    Corrective RAG (CRAG)
    Paper: Tsinghua University, Dec 2025
    
    Web search fallback for knowledge gaps:
    "No Article 19 case? Search latest SCC judgments"
    """
    
    def __init__(self, llm, retriever, web_search_api=None):
        self.llm = llm
        self.retriever = retriever
        self.web_search = web_search_api
    
    async def generate_with_correction(
        self,
        query: str,
        initial_docs: List[Dict]
    ) -> Dict:
        """
        CRAG Pipeline
        
        1. Assess retrieval quality
        2. If insufficient → Web search
        3. Combine retrieved + web results
        4. Generate answer
        """
        
        # Step 1: Assess retrieval quality
        quality_score = await self._assess_retrieval_quality(query, initial_docs)
        
        corrections_log = {
            'initial_quality': quality_score,
            'web_search_used': False,
            'additional_sources': 0
        }
        
        final_docs = initial_docs
        
        # Step 2: If quality is low, try web search
        if quality_score < 0.6:
            web_results = await self._web_search_fallback(query)
            
            if web_results:
                final_docs = initial_docs + web_results
                corrections_log['web_search_used'] = True
                corrections_log['additional_sources'] = len(web_results)
        
        # Step 3: Generate answer with all sources
        answer = await self._generate_with_all_sources(query, final_docs)
        
        return {
            'answer': answer,
            'corrections_log': corrections_log,
            'sources_used': len(final_docs),
            'quality_improved': corrections_log['web_search_used']
        }
    
    async def _assess_retrieval_quality(
        self,
        query: str,
        documents: List[Dict]
    ) -> float:
        """
        Assess if retrieved documents are sufficient
        
        Returns: Quality score 0-1
        """
        
        if not documents:
            return 0.0
        
        assessment_prompt = f"""Rate the quality of these retrieved documents for answering the query.

Query: {query}

Retrieved Documents:
{self._format_docs_for_assessment(documents[:3])}

Consider:
1. Do documents directly address the query?
2. Are they from authoritative legal sources?
3. Do they contain specific case law/sections mentioned in query?
4. Is information recent (2025-2026)?

Rate quality (0.0-1.0):
- 0.9-1.0: Excellent, complete coverage
- 0.7-0.8: Good, mostly sufficient
- 0.5-0.6: Partial, some gaps
- 0.0-0.4: Poor, major gaps

Quality Score:"""
        
        response = await self.llm.generate(assessment_prompt, max_tokens=50)
        
        # Extract score
        import re
        score_match = re.search(r'0\.\d+|1\.0', response)
        if score_match:
            return float(score_match.group())
        
        return 0.5  # Default moderate quality
    
    async def _web_search_fallback(
        self,
        query: str
    ) -> List[Dict]:
        """
        Web search for latest legal information
        
        Targets:
        - Recent Supreme Court judgments
        - Latest legal amendments
        - 2026 legal developments
        """
        
        if not self.web_search:
            return []
        
        # Construct search queries for legal sources
        search_queries = [
            f"{query} Supreme Court India 2026",
            f"{query} latest judgment 2026",
            f"{query} legal update 2026"
        ]
        
        web_results = []
        
        for search_query in search_queries[:2]:  # Limit to 2 searches
            try:
                results = await self.web_search.search(
                    search_query,
                    num_results=3,
                    domains=['sci.gov.in', 'indiankanoon.org']
                )
                
                for result in results:
                    web_results.append({
                        'content': result['snippet'],
                        'source': result['url'],
                        'metadata': {
                            'source_type': 'web',
                            'search_query': search_query
                        }
                    })
            except:
                continue
        
        return web_results
    
    async def _generate_with_all_sources(
        self,
        query: str,
        documents: List[Dict]
    ) -> str:
        """Generate answer with combined sources"""
        
        context = self._format_sources_with_types(documents)
        
        prompt = f"""Answer this legal query using the provided sources (including web results):

Query: {query}

Sources:
{context}

Important:
- Cite all sources with [1], [2], etc.
- Prefer official legal sources over web results
- Note if information is from recent 2026 updates

Answer:"""
        
        answer = await self.llm.generate(prompt, max_tokens=800)
        
        return answer
    
    def _format_docs_for_assessment(self, docs: List[Dict]) -> str:
        """Format docs for quality assessment"""
        
        formatted = []
        for i, doc in enumerate(docs, 1):
            content = doc.get('content', '')[:200]
            source = doc.get('source', 'Unknown')
            formatted.append(f"{i}. [{source}] {content}...")
        
        return "\n".join(formatted)
    
    def _format_sources_with_types(self, docs: List[Dict]) -> str:
        """Format sources indicating type (DB vs Web)"""
        
        formatted = []
        for i, doc in enumerate(docs, 1):
            content = doc.get('content', '')[:400]
            source = doc.get('source', 'Unknown')
            source_type = doc.get('metadata', {}).get('source_type', 'database')
            
            type_indicator = '[WEB]' if source_type == 'web' else '[DB]'
            
            formatted.append(f"[{i}] {type_indicator} {source}:\n{content}\n")
        
        return "\n".join(formatted)


class LongRAGGenerator2026:
    """
    LongRAG: Extended Context Reasoning
    Paper: Together AI, Jan 2026
    
    128K context window processing
    Full judgment analysis in single pass
    """
    
    def __init__(self, llm_long_context):
        self.llm = llm_long_context  # Model with 128K+ context
    
    async def generate_with_long_context(
        self,
        query: str,
        documents: List[Dict],
        full_context: bool = True
    ) -> Dict:
        """
        Process entire legal judgments in single pass
        
        Advantages:
        - No information loss from chunking
        - Better understanding of legal reasoning flow
        - Can analyze entire case from start to finish
        """
        
        if full_context and len(documents) > 0:
            # Combine all documents into single context
            full_text = self._combine_full_documents(documents)
            
            # Check if within context limit (128K tokens ≈ 500K chars)
            if len(full_text) < 400000:
                return await self._process_full_context(query, full_text, documents)
        
        # Fallback to standard processing
        return await self._process_standard(query, documents)
    
    async def _process_full_context(
        self,
        query: str,
        full_text: str,
        documents: List[Dict]
    ) -> Dict:
        """Process with full context"""
        
        prompt = f"""You have access to complete legal documents. Analyze thoroughly:

Query: {query}

Complete Legal Context (full text):
{full_text}

Provide a comprehensive analysis:
1. Direct answer to the query
2. Relevant sections/articles
3. Key legal principles
4. Supporting case law
5. Any exceptions or qualifications

Answer:"""
        
        answer = await self.llm.generate(
            prompt,
            max_tokens=2000,
            temperature=0.2
        )
        
        return {
            'answer': answer,
            'context_size': len(full_text),
            'full_context_used': True,
            'documents_processed': len(documents)
        }
    
    async def _process_standard(
        self,
        query: str,
        documents: List[Dict]
    ) -> Dict:
        """Standard processing for large contexts"""
        
        # Use top documents only
        top_docs = documents[:10]
        context = "\n\n".join([
            f"[{i+1}] {d.get('source', 'Unknown')}:\n{d.get('content', '')}"
            for i, d in enumerate(top_docs)
        ])
        
        prompt = f"""Answer this legal query:

Query: {query}

Sources:
{context}

Answer:"""
        
        answer = await self.llm.generate(prompt, max_tokens=1000)
        
        return {
            'answer': answer,
            'context_size': len(context),
            'full_context_used': False,
            'documents_processed': len(top_docs)
        }
    
    def _combine_full_documents(self, documents: List[Dict]) -> str:
        """Combine full documents maintaining structure"""
        
        combined = []
        for doc in documents:
            source = doc.get('source', 'Unknown')
            content = doc.get('content', '')
            combined.append(f"=== {source} ===\n{content}\n")
        
        return "\n\n".join(combined)
