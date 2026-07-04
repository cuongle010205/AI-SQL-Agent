import streamlit as st

def draw_chart(df):

    if len(df.columns)!=2:

        return

    try:

        chart=df.set_index(df.columns[0])

        st.bar_chart(chart)

    except:

        pass