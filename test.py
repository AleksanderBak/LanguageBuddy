from languagebuddy.chat import LangBuddy

chat = LangBuddy()

for token in chat.get_response("Test"):
    print(token, end="", flush=True)
