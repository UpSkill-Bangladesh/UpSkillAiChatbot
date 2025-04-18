import streamlit as st
from chat_model import query_pipeline


# Streamlit UI
st.title("Chatbot with Ollama DeepSeek 1.5B")
st.write("Ask me anything!")

# Input field for the user query
user_input = st.text_input("Your Query:")

# If the user submits a query, process it
if user_input:
    response = query_pipeline(user_input)
    st.write("Response:", response)