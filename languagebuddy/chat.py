from typing import Any, Generator

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from languagebuddy.prompt_manager import PromptManager
from languagebuddy.settings import settings

load_dotenv()


class Translator:
    def __init__(self, model: str = "gpt-4.1-nano", temperature: float = 0.5) -> None:
        self.model = model
        self.temperature = temperature
        self.prompt_manager = PromptManager(language="danish")
        self.llm = ChatOpenAI(
            model=self.model,
            temperature=self.temperature,
            api_key=settings.openai_key,
            streaming=True,
        )

    def get_response(self, user_input: str) -> Generator[Any, Any, Any]:
        system_prompt = self.prompt_manager.get_system_prompt()
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input),
        ]
        for data in self.llm.stream(messages):
            yield data.content


class LangBuddy:
    def __init__(self, model: str = "gpt-4.1-nano", temperature: float = 0.5) -> None:
        self.model = model
        self.temperature = temperature
        self.prompt_manager = PromptManager(language="danish")
        self.llm = ChatOpenAI(
            model=self.model,
            temperature=self.temperature,
            api_key=settings.openai_key,
            streaming=True,
        )

    def get_response(self, user_input: str) -> Generator[Any, Any, Any]:
        system_prompt = self.prompt_manager.get_system_prompt()
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input),
        ]
        for data in self.llm.stream(messages):
            yield data.content
