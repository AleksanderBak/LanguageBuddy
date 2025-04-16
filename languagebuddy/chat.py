import os
import time
from typing import Any, Generator

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()


class LangBuddy:
    def __init__(self, model: str = "gpt-4.1-nano", temperature: float = 0.5) -> None:
        self.model = model
        self.temperature = temperature
        self.system_prompt = "You are a {name} and you are a {language} expert, always respond in this langauge."
        self.llm = ChatOpenAI(
            model=self.model,
            temperature=self.temperature,
            api_key=os.getenv("OPENAI_API_KEY"),
            streaming=True,
        )

    def get_response(self, prompt) -> Generator[Any, Any, Any]:
        system_prompt = self.system_prompt.format(name="LangBuddy", language="polish")
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=prompt),
        ]
        for data in self.llm.stream(messages):
            yield data.content
