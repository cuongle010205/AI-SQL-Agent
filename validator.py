def validate_sql(sql):
    sql = sql.strip().upper()

    forbidden = [
        "DROP",

    "DELETE",

    "UPDATE",

    "INSERT",

    "ALTER",

    "EXEC",

    "TRUNCATE",

    "MERGE",

    "CREATE",

    "GRANT",

    "REVOKE",

    "DENY",

    "XP_CMDSHELL"
    ]

    if not sql.startswith("SELECT"):
        return False

    for word in forbidden:
        if word in sql:
            return False

    return True