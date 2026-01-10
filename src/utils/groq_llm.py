# utils/groq_llm.py - Groq LLM Interface (FREE)

import os
import httpx
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class GroqLLM:
    """
    Groq LLM Interface - Completely FREE
    
    Models available:
    - llama-3.3-70b-versatile (best quality)
    - llama-3.1-8b-instant (fastest)
    - mixtral-8x7b-32768 (good balance)
    """
    
    def __init__(self, model: str = "llama-3.3-70b-versatile"):
        self.model = model
        self.api_key = os.getenv("GROQ_API_KEY")
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
        
        if not self.api_key:
            logger.warning("GROQ_API_KEY not set - LLM calls will fail")
    
    async def generate(
        self,
        prompt: str,
        system_prompt: str = "You are a helpful legal AI assistant specializing in Indian law. Provide accurate, educational information based on Indian Penal Code, Constitution, and other Indian legal sources. Always include relevant section numbers and legal provisions.",
        max_tokens: int = 1500,
        temperature: float = 0.3
    ) -> str:
        """Generate response using Groq API"""
        
        if not self.api_key:
            return "Error: GROQ_API_KEY not configured. Please set your Groq API key."
        
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    self.base_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": self.model,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt}
                        ],
                        "max_tokens": max_tokens,
                        "temperature": temperature
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    return data["choices"][0]["message"]["content"]
                else:
                    logger.error(f"Groq API error: {response.status_code} - {response.text}")
                    return f"Error: API returned status {response.status_code}"
                    
        except httpx.TimeoutException:
            logger.error("Groq API timeout")
            return "Error: Request timed out. Please try again."
        except Exception as e:
            logger.error(f"Groq API error: {e}")
            return f"Error: {str(e)}"


# Singleton instance
_groq_llm: Optional[GroqLLM] = None

def get_groq_llm() -> GroqLLM:
    """Get Groq LLM instance"""
    global _groq_llm
    if _groq_llm is None:
        _groq_llm = GroqLLM()
    return _groq_llm
