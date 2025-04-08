import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()


class LangBuddy:
    def __init__(self, model="gpt-4o-mini", temperature=0.5):
        self.model = model
        self.temperature = temperature
        self.system_prompt = (
            "You are a {name} and you are a {language} expert, always respond in this langauge."
            "Just make a conversation with the user."
        )
        self.llm = ChatOpenAI(
            model=self.model,
            temperature=self.temperature,
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    def get_response(self, prompt):
        system_prompt = self.system_prompt.format(name="LangBuddy", language="German")
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=prompt),
        ]
        return self.llm.invoke(messages).content
