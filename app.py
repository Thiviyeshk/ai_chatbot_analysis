import streamlit as st
from chatbot import run_query


st.title("📊 AI Data Chatbot")

question = st.text_input("Ask your question:")

if st.button("Run"):
    sql, result = run_query(question)

    st.subheader("Generated SQL:")
    st.code(sql)

    st.subheader("Result:")
    st.write(result)

import streamlit as st

st.title("My AI Chatbot")
st.write("Working successfully 🎉")