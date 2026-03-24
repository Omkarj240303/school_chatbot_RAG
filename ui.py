import streamlit as st
import requests

st.set_page_config(page_title="School Chatbot", layout="centered")

st.title("🎓 School Chatbot")

# chat history store
if "messages" not in st.session_state:
    st.session_state.messages = []

# display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# user input
user_input = st.chat_input("Ask something about school...")

if user_input:
    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # call API
    try:
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": user_input}
        )

        answer = response.json()["answer"]

    except Exception as e:
        answer = "Error connecting to API"

    # show bot response
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)

        