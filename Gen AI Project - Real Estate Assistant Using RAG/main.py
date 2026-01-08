import streamlit as st
from rag import process_urls,generate_answer

st.title("Real Estate Information Agent")

url1 = st.sidebar.text_input("URL-1")
url2 = st.sidebar.text_input("URL-2")
url3 = st.sidebar.text_input("URL-3")

# st.sidebar.button("Process URLs", on_click=lambda: process_urls([url for url in [url1, url2, url3] if url]))
placeholder = st.empty()

process_url_button = st.sidebar.button("Process URLs")
if process_url_button:
    urls = [url for url in (url1, url2, url3) if url!=""]
    if urls:
        with st.spinner("Processing URLs..."):
            for status in process_urls(urls):
                placeholder.text(status)
        st.success("URLs processed and data stored in vector database.")
    else:
        st.warning("Please enter at least one URL.")

query = placeholder.text_input("Question")
if query:
    answer,sources = generate_answer(query)
    st.header("Answer:")
    st.markdown(answer,unsafe_allow_html=True)

    if sources:
        st.subheader("Sources:")
        for source in sources:
            st.write(source) 
