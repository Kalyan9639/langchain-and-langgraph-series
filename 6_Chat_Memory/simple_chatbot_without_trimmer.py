import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

store = {}

# Ensure a unique session_id per user session
if "session_id" not in st.session_state:
    import uuid
    st.session_state.session_id = str(uuid.uuid4())

def get_chat_session(session_id:str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

model = ChatOllama(model = 'gemma3n:e2b')

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are the best communicator. Answer the questions of user with minimum but full answer best to your knowledge'),
        MessagesPlaceholder(variable_name='messages')
    ]
)

chain = prompt|model

with_message_history = RunnableWithMessageHistory(
    chain,
    get_chat_session
)
config = {'configurable': {'session_id': st.session_state.session_id}}

st.title("LLM With Memory")
st.text("#### Basic chatbot for conversation with memory")
user_query = st.text_input("Enter your message")
submit = st.button("Submit")
if submit:
    if user_query:
        response = with_message_history.invoke(user_query,config=config)
        st.markdown(response.content)