import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq


class Configloader():
    def __init__(self):
        print(f"Loading configuration...")
        self.config = load_config()
    
    def __getitem__(self, key):
        return self.config[key]

class ModelLoader():
    def __init__(self):
        model_provider: Literal["groq"] = "groq"
        config: Optional[Configloader] = Field(default=None, exclude=None)

    def model_post_init(self, __context: Any) -> None:
        self.config = Configloader()

    class Config:
        arbitary_types_allowed = True
    
    def load_llm(self):
        """
        Load the LLM model based on the configuration.
        """
        print("Loading LLM model...")
        print(f"Model provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Using Groq model provider, loading Groq model.........")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model=model_name,api_key=groq_api_key)
        elif self.model_provider == "openai":
            pass

        return llm
