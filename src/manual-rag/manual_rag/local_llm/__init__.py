"""Ollama client for local LLM queries"""

import requests
import json
from typing import Optional

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "mistral"):
        self.base_url = base_url
        self.model = model
        self.generate_url = f"{base_url}/api/generate"
        
    def generate(self, prompt: str, context: str = "", system: str = "", 
                 temperature: float = 0.3) -> str:
        """Generate text from local LLM
        
        Args:
            prompt: Main query/prompt
            context: Additional context to include
            system: System prompt for behavior control
            temperature: Sampling temperature (0=deterministic, 1=creative)
            
        Returns:
            Generated text
        """
        full_prompt = prompt
        if context:
            full_prompt = f"Context:\n{context}\n\nQuery:\n{prompt}"
        if system:
            full_prompt = f"System: {system}\n\n{full_prompt}"
            
        try:
            response = requests.post(
                self.generate_url,
                json={
                    "model": self.model,
                    "prompt": full_prompt,
                    "stream": False,
                    "temperature": temperature,
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json().get("response", "").strip()
        except requests.exceptions.ConnectionError:
            raise RuntimeError(
                f"Cannot connect to Ollama at {self.base_url}. "
                "Is it running? Try: ollama serve"
            )
        except Exception as e:
            raise RuntimeError(f"Ollama error: {e}")
    
    def health_check(self) -> bool:
        """Check if Ollama is running and model is available"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                models = response.json().get("models", [])
                model_names = [m.get("name", "").split(":")[0] for m in models]
                return self.model in model_names
            return False
        except:
            return False
