import time
import pandas as pd
import streamlit as st

from planner import need_database
from fake_llm import generate_sql, ask_gemini
from validator import validate_sql
from utils import clean_sql
from SQLexecutor import execute_sql
from explainer import explain
from cache import sql_cache, result_cache
from visualizer import draw_chart
from exporter import export_excel
from logger import log

st.set_page_config(
    page_title="AI SQL Agent",
    layout="wide"
)

st.title("🤖 AI SQL Agent")

# =========================
# Session
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# Sidebar
# =========================

with st.sidebar:

    st.header("⚙ AI SQL Agent")

    st.write("Database : Qlsv")

    st.write("SQL Server")

    st.divider()

    st.header("History")

    for m in st.session_state.messages:

        st.write(f"**{m['role']}**")

        st.write(m["content"])

        st.divider()

    if st.button("🗑 Clear Cache"):

        sql_cache.clear()

        result_cache.clear()

        st.success("Cache cleared!")

# =========================
# Hiển thị chat cũ
# =========================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =========================
# Input
# =========================

prompt = st.chat_input("Nhập câu hỏi...")

if prompt:

    start = time.time()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.write(prompt)

    # =========================
    # Không cần Database
    # =========================

    if not need_database(prompt):

        with st.spinner("Gemini đang trả lời..."):

            reply = ask_gemini(prompt)

        with st.chat_message("assistant"):

            st.write(reply)

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":reply
            }
        )

        st.stop()

    # =========================
    # SQL
    # =========================

    with st.spinner("Đang sinh SQL..."):

        if prompt in sql_cache:

            sql = sql_cache[prompt]

        else:

            sql = generate_sql(
                prompt,
                st.session_state.messages
            )

            sql_cache[prompt] = sql

    sql = clean_sql(sql)

    log(prompt, sql)

    # =========================
    # Validate
    # =========================

    if not validate_sql(sql):

        st.error("SQL không hợp lệ")

        st.stop()

    # =========================
    # Execute
    # =========================

    if sql in result_cache:

        columns, rows = result_cache[sql]

    else:

        columns, rows = execute_sql(sql)

        result_cache[sql] = (columns, rows)

    df = pd.DataFrame(rows, columns=columns)

    # =========================
    # Explain
    # =========================

    answer = explain(prompt, df)

    end = time.time()

    # =========================
    # Assistant
    # =========================

    with st.chat_message("assistant"):

        st.subheader("📝 SQL")

        st.code(sql, language="sql")

        st.subheader("📊 Result")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.success(f"{len(df)} rows")

        draw_chart(df)

        st.download_button(
            "📥 Download Excel",
            export_excel(df),
            "result.xlsx"
        )

        st.subheader("🤖 Explanation")

        st.write(answer)

        st.caption(
            f"⏱ {end-start:.2f} s"
        )

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )