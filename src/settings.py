from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parent.parent / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

    llm_api_key: str = Field(description="Ключ от LLM API")
    llm_base_url: str = Field(default="https://ollama.com/v1", description="Эндпоинт от LLM API")
    llm_model: str = Field(default="gemma4:31b", description="Название LLM")
