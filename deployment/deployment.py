# deployment.py - Production Setup

from prometheus_client import Counter, Histogram, Gauge
import time
import logging
from typing import Dict
import json
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.intent_analyzer import EducationalIntentAnalyzer
from src.legal_knowledge import format_punishment_answer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Monitoring metrics
query_counter = Counter('rag_queries_total', 'Total RAG queries')
query_duration = Histogram('rag_query_duration_seconds', 'RAG query duration')
hallucination_rate = Gauge('hallucination_rate', 'Current hallucination rate')
retrieval_quality = Gauge('retrieval_quality', 'Current retrieval quality')
error_counter = Counter('rag_errors_total', 'Total RAG errors')


class ProductionRAG:
    """Production-ready RAG system with monitoring"""
    
    def __init__(self, config_file: str = "config/config.json"):
        self.logger = logging.getLogger(__name__)
        self.intent_analyzer = EducationalIntentAnalyzer()
        self.config = {}
        self.load_config(config_file)
        
        self.logger.info("Production RAG system initialized")
    
    def load_config(self, config_file: str):
        """Load configuration from file"""
        
        try:
            with open(config_file) as f:
                self.config = json.load(f)
            self.logger.info(f"Configuration loaded from {config_file}")
        except FileNotFoundError:
            self.logger.warning(f"Config file {config_file} not found, using defaults")
    
    async def handle_query(self, query: str) -> Dict:
        """Handle query with monitoring"""
        
        start = time.time()
        query_counter.inc()
        
        try:
            self.logger.info(f"Processing query: {query[:100]}...")
            
            # Use intent analyzer
            analysis = self.intent_analyzer.analyze(query)
            
            if analysis["type"] == "PUNISHMENT_EDUCATION":
                answer = format_punishment_answer(analysis.get('crime_type', 'murder'))
            else:
                answer = f"Query received: {query}"
            
            duration = time.time() - start
            query_duration.observe(duration)
            
            self.logger.info(f"Query processed in {duration:.2f}s")
            
            return {
                'answer': answer,
                'intent': analysis['type'],
                'confidence': analysis['confidence'],
                'processing_time': duration
            }
        
        except Exception as e:
            error_counter.inc()
            self.logger.error(f"Error processing query: {str(e)}")
            raise


class HealthMonitor:
    """Monitor system health"""
    
    def __init__(self, rag_system: ProductionRAG):
        self.rag = rag_system
        self.logger = logging.getLogger(__name__)
    
    def check_health(self) -> Dict:
        """Perform health check"""
        
        health_status = {
            'status': 'healthy',
            'components': {},
            'timestamp': time.time()
        }
        
        # Check intent analyzer
        try:
            if self.rag.intent_analyzer:
                health_status['components']['intent_analyzer'] = 'operational'
            else:
                health_status['components']['intent_analyzer'] = 'unavailable'
                health_status['status'] = 'degraded'
        except Exception as e:
            health_status['components']['intent_analyzer'] = f'error: {str(e)}'
            health_status['status'] = 'unhealthy'
        
        return health_status
    
    def get_metrics(self) -> Dict:
        """Get current metrics"""
        
        return {
            'total_queries': query_counter._value.get(),
            'current_hallucination_rate': hallucination_rate._value.get(),
            'retrieval_quality': retrieval_quality._value.get(),
            'total_errors': error_counter._value.get()
        }


# Example usage
if __name__ == "__main__":
    import asyncio
    
    async def main():
        # Initialize production RAG
        prod_rag = ProductionRAG()
        
        # Test query
        result = await prod_rag.handle_query(
            "What is the punishment for murder under IPC Section 302?"
        )
        
        print(f"Answer: {result['answer'][:200]}...")
        print(f"Intent: {result['intent']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Processing Time: {result['processing_time']:.2f}s")
    
    asyncio.run(main())
