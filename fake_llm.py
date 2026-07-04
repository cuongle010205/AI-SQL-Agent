from schema import get_schema
from LLM import ask_gemini
from memory import build_history

def generate_sql(question, messages):

    schema = get_schema()

    history = build_history(messages)

    prompt = f"""
Bạn là chuyên gia SQL Server.

Đây là schema của database:

{schema}

Nhiệm vụ:
- Chuyển câu hỏi tiếng Việt thành SQL Server.
- Chỉ dùng bảng và cột có trong schema.
- Chỉ trả về đúng một câu lệnh SQL.
- Không markdown.
- Không giải thích.
- Không thêm bất kỳ văn bản nào khác.

Ví dụ:

Q: Có bao nhiêu sinh viên?
A:
SELECT COUNT(*) FROM SinhVien;

Q: Hiển thị 5 sinh viên đầu tiên
A:
SELECT TOP 5 * FROM SinhVien;
History:

{history}


Câu hỏi:
{question}
Quy tắc:
1. Chỉ trả về một câu lệnh SQL Server.
2. Chỉ dùng SELECT.
3. Không markdown.
4. Không giải thích.
5. Nếu câu hỏi hiện tại phụ thuộc lịch sử thì phải sử dụng lịch sử để suy luận.
"""

    print("===== PROMPT =====")
    print(prompt)

    sql = ask_gemini(prompt)

    print("===== GEMINI =====")
    print(sql)

    return sql