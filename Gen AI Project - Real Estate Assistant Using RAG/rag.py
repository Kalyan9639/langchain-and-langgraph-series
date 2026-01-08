from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

EMBEDDING_MODEL='ibm-granite/granite-embedding-small-english-r2'
COLLECTION_NAME='real_estate'
VECTORSTORE_PATH="./vector_db"

llm = None
vector_db = None

def initialize_elements():
    '''
    This function initializes the embedding model and vector database.
    
    :return: embedding model and vector database
    '''
    global llm, vector_db

    if llm is None:
        llm = ChatGroq(model='openai/gpt-oss-20b',temperature=0.9,max_tokens=2500)

    if vector_db is None:
        embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )
        vector_db = Chroma(
            collection_name=COLLECTION_NAME,
            persist_directory=VECTORSTORE_PATH,
            embedding_function=embedding_model,
        )

    return llm, vector_db

def process_urls(urls):
        '''
        This function scrapes data from urls and stores it in a vector database.
        
        :param urls: input urls
        :return: 
        '''
        # print("============Initializing components============")
        yield "============Initializing components ✅============"
        initialize_elements()

        vector_db.reset_collection()

        # print("============Loading The URLs============")
        yield "============Loading The URLs ✅============"
        loader = UnstructuredURLLoader(urls=urls)
        data = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", ".", " "],
            chunk_size=1000,
            chunk_overlap=200,
        )
        yield "============Splitting The Data ✅============"
        # print("============Splitting The Data============")
        documents = splitter.split_documents(data)
        uuids= [str(uuid4()) for _ in range(len(documents))]
        # print("============Adding The Data To Vector DB============")
        yield "============Adding The Data To Vector DB ============"
        vector_db.add_documents(
            documents=documents,
            ids=uuids,
            
        )

        yield 'Done Adding Docs to the Vector DB ✅'

def generate_answer(query):
    if not vector_db:
        raise RuntimeError("Vector database is not initialized.")
    
    context = vector_db.similarity_search(query, k=3)
    sources = []

    for doc in context:
        sources.append(doc.metadata.get("source"))


    prompt = f""" 
You are a helpful real estate assistant. Use the following context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
Context: {context}
"""

    template = ChatPromptTemplate.from_messages([
        SystemMessage(content=prompt),
        HumanMessage(query)
    ])

    chain = template | llm

    result = chain.invoke({'query':query})
    print(result)

    return result.content,sources



if __name__=="__main__":
    urls = [
         "https://propertywala.com/blog/how-tos/optimizing-real-estate-taxes-for-nri-owners-of-panchkula-properties",
         "https://propertywala.com/blog/trends/mid-tier-housing-vs-luxury-navigating-panchkulas-three-tier-real-estate-market"
    ]
    
    process_urls(urls)
    query = "As a real estate analyst who have experience in explainig or helping new people understanding things simply, Give me a detailed and simple summary for all the topics that you have with you"
    answer,sources = generate_answer(query)
    print("\n\nAnswer:", answer)
    print("\n\nSources:", sources)

    with open("./response.md",'w',encoding='utf-8') as f:
         f.write(f'# {query}\n\n {answer}')

    