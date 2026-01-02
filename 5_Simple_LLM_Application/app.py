from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_community.document_loaders import WikipediaLoader
import streamlit as st
from langchain.prompts import ChatPromptTemplate
import time

def load_and_split_docs(query):
    loader = WikipediaLoader(query=query)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = loader.load()
    splitted_docs = splitter.split_documents(documents)
    return splitted_docs

def ask_llm(query):
    docs = load_and_split_docs(query)
    context = docs[0].page_content if docs else "No relevant information found."
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that answers questions based on the provided context."),
        ("human", "{context} \n\n Question: {query}"),
    ])
    llm = ChatOllama(model="gemma3n:e2b", temperature=0.1, max_tokens=1000)
    response = llm.invoke(query)
    return response

st.title("✈️AIPEDIA - Your AI-Powered Wikipedia Search")
st.write("***This application will answer any question that you ask by searching Wikipedia. It uses a LLM to generate the response.***")
query = st.text_input("Ask a question", key="query")

if st.button("Search"):
    if query:
        st.spinner("Searching...", show_time=True)
        st.write("🔍 Searching Wikipedia and generating a response...")
        start_time = time.time()
        response = ask_llm(query)
        end_time = time.time()
        elapsed = end_time - start_time
        st.success(f"⏱️ Time taken: {elapsed:.2f} seconds")
        st.write("### Response from LLM:")
        st.write("Response:")
        st.write(response.content)

    