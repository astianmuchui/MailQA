import streamlit as st
from langchain_convo import preprocess_emails, initialize_embeddings_and_vectorstore, initialize_conversation_chain
import time
api_key =  st.secrets["openai"]["api_key"]

st.set_page_config(page_title="Mail QA", page_icon="public\145862897_padded_logo.png", layout="centered")
st.title("Mail QA")

data = preprocess_emails()
vectorstore = initialize_embeddings_and_vectorstore(data)
conversation_chain = initialize_conversation_chain(vectorstore,api_key)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("You:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        if prompt.lower() == "quit":
            assistant_response = "Goodbye!"
        else:
            assistant_response = conversation_chain.run(prompt)
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.02)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
