from schema import get_schema

schema = get_schema()

def build_prompt(question):

    prompt = f"""

Bạn là chuyên gia SQL Server.

Schema:

{schema}

Chỉ trả về câu SQL.

Question:

{question}

"""

    return prompt
