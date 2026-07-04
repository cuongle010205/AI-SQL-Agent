def need_database(question):

    keywords=[

        "bao nhiêu",

        "liệt kê",

        "danh sách",

        "đếm",

        "thống kê",

        "tìm",

        "xem"

    ]

    q=question.lower()

    return any(k in q for k in keywords)