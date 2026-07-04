def build_history(messages):

    if not messages:
        return ""

    history = ""

    for msg in messages:
        history += f"{msg['role']}:\n{msg['content']}\n\n"

    return history