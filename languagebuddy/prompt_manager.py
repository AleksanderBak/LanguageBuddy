from jinja2 import Template


class PromptManager:
    def __init__(self, language):
        self.language = language
        self.template = Template(
            "You are a are a {{ language }} expert, always respond in this langauge."
        )
        self.system_prompt = self.template.render(language=self.language)

    def get_system_prompt(self):
        return self.system_prompt
