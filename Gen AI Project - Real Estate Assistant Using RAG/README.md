<div align="center">

# 🏠 Real Estate Intel-Agent
**High-Performance RAG Pipeline for Automated Property Market Analysis**

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-white?style=for-the-badge&logo=chainlink&logoColor=black)](https://langchain.com/)
[![VectorDB](https://img.shields.io/badge/VectorDB-Chroma-orange?style=for-the-badge)](https://www.trychroma.com/)
[![Model](https://img.shields.io/badge/LLM-Groq--GPT--OSS-green?style=for-the-badge)](https://groq.com/)

---

[Explore Demo](#-usage) • [Report Bug](https://github.com/Kalyan9639/langchain-and-langgraph-series/issues) • [Request Feature](https://github.com/your-username/repo/issues)

</div>

## 📖 Overview

**Real Estate Intel-Agent** is a sophisticated Retrieval-Augmented Generation (RAG) platform designed to synthesize vast amounts of real estate web data into actionable insights. By combining **IBM's Granite Embeddings** with the extreme inference speed of **Groq**, this agent allows users to query complex property blogs, tax laws, and market trends with zero-latency response times and full source transparency.

### 🌟 Key Capabilities
- **Dynamic Web Ingestion**: Parallel processing of multiple property-related URLs using `UnstructuredURLLoader`.
- **Hybrid Context Retrieval**: Semantic search optimized via `RecursiveCharacterTextSplitter` for high-context retention.
- **Embedded Intelligence**: Leverages `ibm-granite/granite-embedding-small-english-r2` for superior semantic mapping in the real estate domain.
- **Source Attribution**: Every response is back-linked to the source document, ensuring data integrity and auditability.

---

## 🏗️ System Architecture

The pipeline is engineered for modularity and scalability:

1.  **Ingestion Layer**: Scrapes raw HTML and cleans data using the `Unstructured` framework.
2.  **Transformation Layer**: Implements a recursive splitting strategy ($Chunk Size: 1000$, $Overlap: 200$) to maintain semantic continuity.
3.  **Vector Store Layer**: Persists embeddings in a local `Chroma` instance for rapid retrieval without redundant API calls.
4.  **Inference Layer**: Orchestrates a `ChatPromptTemplate` chain via **Groq** to generate context-grounded responses.

---

## 🛠️ Technical Specifications

| Component | Implementation |
| :--- | :--- |
| **Embeddings** | `ibm-granite/granite-embedding-small-english-r2` |
| **LLM Engine** | `openai/gpt-oss-20b` (via Groq Cloud) |
| **Vector Database** | ChromaDB (Local Persistence) |
| **Framework** | LangChain Expression Language (LCEL) |
| **Concurrency** | Python Generator-based Status Streaming |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A [Groq Cloud](https://console.groq.com/) API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/real-estate-intel-agent.git](https://github.com/your-username/real-estate-intel-agent.git)
   cd real-estate-intel-agent
   ```
   
2. **Environment Configuration**  Create a .env file in the root directory and populate your credentials:
```
GROQ_API_KEY=your_secure_api_key_here
```

3. **Dependency Deployment**
```
pip install -r requirements.txt
```

4. **Launch Interface**

```
streamlit run main.py
```

## 🕹️ Usage Guide

1.  **Knowledge Injection**: Input up to 3 URLs in the sidebar (e.g., market reports, tax guidelines).
2.  **Indexing**: Click `Process URLs`. The system will tokenize and embed the data into the local vector store.
3.  **Contextual Querying**: Ask complex questions like *"Summarize the tax implications for NRI property owners in Panchkula."*
4.  **Verification**: Expand the **Sources** section to view the specific documentation utilized by the LLM.

---

## 📂 Directory Structure

```text
├── main.py              # Streamlit UI & Application Logic
├── rag.py               # Core RAG Engine (Scraping, Vector Store, LLM Chain)
├── requirements.txt     # Python Project Dependencies
├── .env                 # API Keys & Secrets (Not to be committed)
└── vector_db/           # ChromaDB Persistent Storage
```

## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create.
1. Fork the Project.
2. Create your Feature Branch (git checkout -b feature/AmazingFeature).
3. Commit your Changes (git commit -m 'Add some AmazingFeature').
4. Push to the Branch (git push origin feature/AmazingFeature).
5. Open a Pull Request.

---

## 📄 License
Distributed under the MIT License. See LICENSE for more information.

<div align="center"> Built with ❤️ for the Real Estate Tech Community </div>
