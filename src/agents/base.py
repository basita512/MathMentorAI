"""Base agent class."""
from langchain_groq import ChatGroq
from src.utils.config import config

class BaseAgent:
    def __init__(self, system_prompt: str, temperature: float = None):
        self.llm = ChatGroq(
            api_key=config.GROQ_API_KEY,
            model=config.LLM_MODEL,
            temperature=temperature or config.GROQ_TEMPERATURE
        )
        self.system_prompt = system_prompt
    
    def invoke(self, user_message: str) -> str:
        """Invoke agent with message."""
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message}
        ]
        response = self.llm.invoke(messages)
        return response.content
