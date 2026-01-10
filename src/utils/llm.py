# utils/llm.py - LLM Interface for 2026

import os
from typing import List, Optional
import openai
from anthropic import AsyncAnthropic


class LLMInterface:
    """
    LLM Interface supporting multiple models
    
    2026 Stack:
    - Primary: Llama-3.2-11B (fast, efficient)
    - Critic: Qwen2.5-Coder-14B (better at code/logic)
    - Long Context: Claude 3.5 Sonnet (128K context)
    """
    
    def __init__(self, model_name: str = "llama-3.2-11b"):
        self.model_name = model_name
        self.api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    
    async def generate(
        self,
        prompt: str,
        max_tokens: int = 1000,
        temperature: float = 0.3,
        **kwargs
    ) -> str:
        """Generate text completion"""
        
        if "gpt" in self.model_name or "llama" in self.model_name:
            return await self._generate_openai(prompt, max_tokens, temperature)
        elif "claude" in self.model_name:
            return await self._generate_anthropic(prompt, max_tokens, temperature)
        else:
            # Default to OpenAI-compatible API
            return await self._generate_openai(prompt, max_tokens, temperature)
    
    async def _generate_openai(
        self,
        prompt: str,
        max_tokens: int,
        temperature: float
    ) -> str:
        """OpenAI-compatible generation"""
        
        try:
            client = openai.AsyncOpenAI(api_key=self.api_key)
            
            response = await client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a legal AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            return response.choices[0].message.content
        except Exception as e:
            # Re-raise the exception so the caller can handle it
            raise
    
    async def _generate_anthropic(
        self,
        prompt: str,
        max_tokens: int,
        temperature: float
    ) -> str:
        """Anthropic Claude generation"""
        
        try:
            client = AsyncAnthropic(api_key=self.api_key)
            
            response = await client.messages.create(
                model=self.model_name,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return response.content[0].text
        except Exception as e:
            # Re-raise the exception so the caller can handle it
            raise


# Singleton instances
_llm_primary = None
_llm_critic = None
_llm_long_context = None


def get_llm_primary() -> LLMInterface:
    """Get primary LLM (Llama-3.2-11B)"""
    global _llm_primary
    
    if _llm_primary is None:
        model = os.getenv("LLM_PRIMARY_MODEL", "llama-3.2-11b")
        _llm_primary = LLMInterface(model)
    
    return _llm_primary


def get_llm_critic() -> LLMInterface:
    """Get critic LLM (Qwen2.5-Coder-14B)"""
    global _llm_critic
    
    if _llm_critic is None:
        model = os.getenv("LLM_CRITIC_MODEL", "qwen2.5-coder-14b")
        _llm_critic = LLMInterface(model)
    
    return _llm_critic


def get_llm_long_context() -> LLMInterface:
    """Get long context LLM (Claude 3.5 Sonnet)"""
    global _llm_long_context
    
    if _llm_long_context is None:
        model = os.getenv("LLM_LONG_MODEL", "claude-3-5-sonnet-20241022")
        _llm_long_context = LLMInterface(model)
    
    return _llm_long_context
