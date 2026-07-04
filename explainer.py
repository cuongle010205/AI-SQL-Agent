def explain(question, df):

    if df.empty:
        return "Không tìm thấy dữ liệu phù hợp."

    # Câu hỏi đếm
    if len(df) == 1 and len(df.columns) == 1:

        value = df.iloc[0,0]

        return f"Kết quả là **{value}**."

    # Một bản ghi
    if len(df) == 1:

        return "Đã tìm thấy 1 bản ghi."

    return f"Truy vấn trả về **{len(df)}** bản ghi."