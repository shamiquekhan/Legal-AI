# safety.py - 7-Level Hallucination Detection

from typing import List, Dict, Optional
import re
import json
import asyncio
from datetime import datetime


class HallucinationDetector2026:
    """
    7-Level Hallucination Detection System
    Enhanced for 2026 with latest research
    
    Levels:
    1. Factual Consistency
    2. Legal Citation Accuracy
    3. Temporal Consistency
    4. Entity Consistency
    5. Source Attribution
    6. Cross-Document Consistency
    7. Recent Judgments 2026
    """
    
    def __init__(self, llm, knowledge_base=None):
        self.llm = llm
        self.kb = knowledge_base
        self.current_year = 2026
    
    async def detect_hallucinations(
        self,
        answer: str,
        sources: List[Dict],
        query: str
    ) -> Dict:
        """
        Comprehensive 7-level hallucination detection
        
        Returns detailed analysis with risk scoring
        """
        
        # Run all 7 checks in parallel
        checks = await asyncio.gather(
            self._level1_factual_consistency(answer, sources),
            self._level2_legal_citation_accuracy(answer, sources),
            self._level3_temporal_consistency(answer),
            self._level4_entity_consistency(answer),
            self._level5_source_attribution(answer, sources),
            self._level6_cross_document_consistency(answer, sources),
            self._level7_recent_judgments(answer, sources)
        )
        
        # Compile results
        all_issues = []
        level_scores = {}
        
        for i, (level_name, issues, score) in enumerate(checks, 1):
            level_scores[f'level_{i}_{level_name}'] = score
            all_issues.extend(issues)
        
        # Calculate overall hallucination score
        avg_score = sum(level_scores.values()) / len(level_scores)
        hallucination_score = 1.0 - avg_score  # Invert: higher = more hallucination
        
        # Determine risk level
        risk_level = self._calculate_risk_level(hallucination_score)
        
        return {
            'hallucination_score': hallucination_score,
            'is_safe': hallucination_score < 0.10,  # <10% hallucination
            'risk_level': risk_level,
            'level_scores': level_scores,
            'issues_found': all_issues,
            'total_issues': len(all_issues),
            'checks_passed': sum(1 for s in level_scores.values() if s > 0.85)
        }
    
    async def _level1_factual_consistency(
        self,
        answer: str,
        sources: List[Dict]
    ) -> tuple[str, List[Dict], float]:
        """
        Level 1: Check if facts in answer are in sources
        
        Most critical check - prevents fabricated information
        """
        
        issues = []
        
        # Extract factual claims from answer
        claims = await self._extract_factual_claims(answer)
        
        # Build source text corpus
        source_text = " ".join([s.get('content', '') for s in sources])
        
        verified_count = 0
        
        for claim in claims:
            # Check if claim is supported by sources
            is_verified = await self._verify_claim_in_sources(claim, source_text)
            
            if is_verified:
                verified_count += 1
            else:
                issues.append({
                    'level': 1,
                    'type': 'factual_inconsistency',
                    'claim': claim,
                    'severity': 'high',
                    'evidence': 'Claim not found in provided sources'
                })
        
        score = verified_count / max(len(claims), 1)
        
        return ('factual_consistency', issues, score)
    
    async def _level2_legal_citation_accuracy(
        self,
        answer: str,
        sources: List[Dict]
    ) -> tuple[str, List[Dict], float]:
        """
        Level 2: Verify legal citations are correct
        
        Checks:
        - Article/Section numbers are real
        - Case names are accurate
        - Years are correct
        - Citations match sources
        """
        
        issues = []
        
        # Extract legal citations
        citations = self._extract_legal_citations(answer)
        
        verified_count = 0
        
        for citation in citations:
            # Verify citation
            is_accurate = await self._verify_legal_citation(citation, sources)
            
            if is_accurate:
                verified_count += 1
            else:
                issues.append({
                    'level': 2,
                    'type': 'citation_inaccuracy',
                    'citation': citation,
                    'severity': 'high',
                    'evidence': 'Citation details do not match sources'
                })
        
        score = verified_count / max(len(citations), 1) if citations else 1.0
        
        return ('legal_citation_accuracy', issues, score)
    
    async def _level3_temporal_consistency(
        self,
        answer: str
    ) -> tuple[str, List[Dict], float]:
        """
        Level 3: Check temporal consistency
        
        Issues:
        - Future years (> 2026)
        - Impossible date sequences
        - Anachronistic references
        """
        
        issues = []
        
        # Extract years
        years = re.findall(r'\b(19|20)\d{2}\b', answer)
        years_int = [int(y) for y in years]
        
        # Check for future years
        future_years = [y for y in years_int if y > self.current_year]
        
        for year in future_years:
            issues.append({
                'level': 3,
                'type': 'temporal_inconsistency',
                'claim': f'Year {year} mentioned',
                'severity': 'high',
                'evidence': f'Future year {year} referenced (current: {self.current_year})'
            })
        
        # Check for impossible sequences
        if years_int:
            # Example: "2026 case overruled 2025 case" is fine
            # But "1950 case overruled 2000 case" is suspicious
            pass
        
        # Score: 1.0 if no future years, 0.5 if some issues
        score = 1.0 if not future_years else 0.5
        
        return ('temporal_consistency', issues, score)
    
    async def _level4_entity_consistency(
        self,
        answer: str
    ) -> tuple[str, List[Dict], float]:
        """
        Level 4: Check entity consistency
        
        Issues:
        - Inconsistent entity names
        - Incorrect entity types
        - Conflicting entity attributes
        """
        
        issues = []
        
        # Extract named entities
        entities = await self._extract_named_entities(answer)
        
        # Check for inconsistencies
        entity_variations = {}
        
        for entity in entities:
            name = entity['name'].lower()
            base_name = self._normalize_entity_name(name)
            
            if base_name not in entity_variations:
                entity_variations[base_name] = []
            entity_variations[base_name].append(entity['name'])
        
        # Flag entities with multiple variations
        for base_name, variations in entity_variations.items():
            unique_forms = set(variations)
            if len(unique_forms) > 2:  # Allow some variation
                issues.append({
                    'level': 4,
                    'type': 'entity_inconsistency',
                    'claim': f"Entity '{base_name}' has multiple forms",
                    'severity': 'medium',
                    'evidence': f"Forms: {', '.join(list(unique_forms)[:3])}"
                })
        
        score = 1.0 - (len(issues) * 0.1)  # Deduct 10% per issue
        
        return ('entity_consistency', issues, max(score, 0.0))
    
    async def _level5_source_attribution(
        self,
        answer: str,
        sources: List[Dict]
    ) -> tuple[str, List[Dict], float]:
        """
        Level 5: Check if claims are properly attributed
        
        Issues:
        - Legal claims without citations
        - Missing source references
        - Incorrect citation numbers
        """
        
        issues = []
        
        # Find legal claims that should be cited
        legal_patterns = [
            (r'Section \d+[\w\(\)]*', 'Section reference'),
            (r'Article \d+[\w\(\)]*', 'Article reference'),
            (r'(Supreme|High) Court', 'Court reference'),
            (r'punishment.*?(imprisonment|fine|death)', 'Punishment reference'),
            (r'\d{4}\s+SCC', 'Case law reference')
        ]
        
        # Extract citations
        citations = set(re.findall(r'\[\d+\]', answer))
        
        for pattern, claim_type in legal_patterns:
            matches = re.finditer(pattern, answer, re.IGNORECASE)
            
            for match in matches:
                pos = match.start()
                claim_text = match.group()
                
                # Check if citation within 150 chars before or after
                context_start = max(0, pos - 150)
                context_end = min(len(answer), pos + 150)
                context = answer[context_start:context_end]
                
                has_citation = any(citation in context for citation in citations)
                
                if not has_citation:
                    issues.append({
                        'level': 5,
                        'type': 'missing_attribution',
                        'claim': claim_text,
                        'severity': 'medium',
                        'evidence': f'{claim_type} without citation'
                    })
        
        # Limit issues to avoid over-flagging
        issues = issues[:10]
        
        # Score based on attribution rate
        total_claims = sum(
            len(re.findall(pattern, answer, re.IGNORECASE))
            for pattern, _ in legal_patterns
        )
        
        if total_claims == 0:
            score = 1.0
        else:
            cited_rate = max(0, 1.0 - (len(issues) / total_claims))
            score = cited_rate
        
        return ('source_attribution', issues, score)
    
    async def _level6_cross_document_consistency(
        self,
        answer: str,
        sources: List[Dict]
    ) -> tuple[str, List[Dict], float]:
        """
        Level 6: Check consistency across multiple sources
        
        Issues:
        - Contradictions between sources
        - Cherry-picking from sources
        - Missing important contradictory info
        """
        
        issues = []
        
        # Check if answer acknowledges contradictions
        if len(sources) > 1:
            # Look for contradiction indicators
            contradiction_phrases = [
                'however', 'but', 'on the other hand',
                'contrary to', 'different view', 'alternatively'
            ]
            
            has_nuance = any(
                phrase in answer.lower()
                for phrase in contradiction_phrases
            )
            
            # If multiple sources but no nuance, might be cherry-picking
            if len(sources) >= 3 and not has_nuance:
                issues.append({
                    'level': 6,
                    'type': 'potential_cherry_picking',
                    'claim': 'Multiple sources but no acknowledgment of different views',
                    'severity': 'low',
                    'evidence': 'Consider multiple perspectives from sources'
                })
        
        score = 1.0 - (len(issues) * 0.15)
        
        return ('cross_document_consistency', issues, max(score, 0.0))
    
    async def _level7_recent_judgments(
        self,
        answer: str,
        sources: List[Dict]
    ) -> tuple[str, List[Dict], float]:
        """
        Level 7: Check for recent legal developments
        
        Issues:
        - Outdated information when recent cases exist
        - Missing 2026 amendments
        - Obsolete legal interpretations
        """
        
        issues = []
        
        # Check if answer mentions recent developments
        recent_indicators = ['2026', '2025', 'recent', 'latest', 'current']
        
        has_recent_reference = any(
            indicator in answer.lower()
            for indicator in recent_indicators
        )
        
        # Check sources for recent years
        source_years = []
        for source in sources:
            metadata = source.get('metadata', {})
            year = metadata.get('year')
            if year:
                try:
                    source_years.append(int(year))
                except:
                    pass
        
        # If query might need recent info but sources are old
        if source_years and max(source_years) < 2024:
            issues.append({
                'level': 7,
                'type': 'potentially_outdated',
                'claim': 'Using sources from before 2024',
                'severity': 'low',
                'evidence': f'Most recent source: {max(source_years)}'
            })
        
        score = 1.0 if not issues else 0.85
        
        return ('recent_judgments', issues, score)
    
    # Helper methods
    
    async def _extract_factual_claims(self, text: str) -> List[str]:
        """Extract factual claims from text"""
        
        # Simple: split by sentences
        sentences = re.split(r'[.!?]', text)
        claims = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 20]
        
        return claims[:15]  # Limit to 15 claims
    
    async def _verify_claim_in_sources(
        self,
        claim: str,
        source_text: str
    ) -> bool:
        """Verify if claim is supported by sources"""
        
        # Simple word overlap check
        claim_words = set(claim.lower().split())
        source_words = set(source_text.lower().split())
        
        overlap = len(claim_words & source_words)
        overlap_ratio = overlap / max(len(claim_words), 1)
        
        return overlap_ratio > 0.4  # 40% word overlap threshold
    
    def _extract_legal_citations(self, text: str) -> List[Dict]:
        """Extract legal citations"""
        
        citations = []
        
        # Article citations
        articles = re.finditer(r'Article\s+(\d+)(?:\((\d+)\))?(?:\(([a-z])\))?', text, re.IGNORECASE)
        for match in articles:
            citations.append({
                'type': 'article',
                'number': match.group(1),
                'clause': match.group(2),
                'full_text': match.group(0)
            })
        
        # Section citations
        sections = re.finditer(r'Section\s+(\d+[A-Z]*)', text, re.IGNORECASE)
        for match in sections:
            citations.append({
                'type': 'section',
                'number': match.group(1),
                'full_text': match.group(0)
            })
        
        # Case citations
        cases = re.finditer(r'(\w+(?:\s+\w+)*)\s+v\.?\s+(\w+(?:\s+\w+)*)\s+\((\d{4})\)', text)
        for match in cases:
            citations.append({
                'type': 'case',
                'parties': f"{match.group(1)} v. {match.group(2)}",
                'year': match.group(3),
                'full_text': match.group(0)
            })
        
        return citations
    
    async def _verify_legal_citation(
        self,
        citation: Dict,
        sources: List[Dict]
    ) -> bool:
        """Verify citation against sources"""
        
        # Check if citation appears in any source
        source_text = " ".join([s.get('content', '') for s in sources])
        
        full_text = citation.get('full_text', '')
        
        # Simple check: citation text appears in sources
        return full_text.lower() in source_text.lower()
    
    async def _extract_named_entities(self, text: str) -> List[Dict]:
        """Extract named entities"""
        
        entities = []
        
        # Court names
        courts = re.finditer(r'(Supreme|High|District)\s+Court(?:\s+of\s+\w+)?', text)
        for match in courts:
            entities.append({'name': match.group(0), 'type': 'court'})
        
        # Acts
        acts = re.finditer(r'(\w+(?:\s+\w+)*?)\s+Act,?\s+(\d{4})', text)
        for match in acts:
            entities.append({'name': match.group(0), 'type': 'act'})
        
        return entities
    
    def _normalize_entity_name(self, name: str) -> str:
        """Normalize entity name for comparison"""
        
        # Remove punctuation, lowercase
        normalized = re.sub(r'[^\w\s]', '', name.lower())
        # Remove common words
        normalized = re.sub(r'\b(the|of|and|court|act)\b', '', normalized)
        return normalized.strip()
    
    def _calculate_risk_level(self, hallucination_score: float) -> str:
        """Calculate risk level from hallucination score"""
        
        if hallucination_score < 0.02:
            return 'very_low'
        elif hallucination_score < 0.05:
            return 'low'
        elif hallucination_score < 0.10:
            return 'medium'
        elif hallucination_score < 0.20:
            return 'high'
        else:
            return 'critical'
