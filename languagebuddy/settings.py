from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    openai_key: str = Field(validation_alias="OPENAI_API_KEY")


settings = Settings()
