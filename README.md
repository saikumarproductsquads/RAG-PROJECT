# 🍕 Pizza Restaurant Review Assistant (RAG Chatbot)

A **Retrieval-Augmented Generation (RAG)** based chatbot that answers questions about a pizza restaurant using real customer reviews — powered by local LLMs via Ollama.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange)

---

## 🎯 What This Project Does

- Loads real pizza restaurant customer reviews from a CSV file
- Converts reviews into vector embeddings using **mxbai-embed-large**
- Stores vectors in **ChromaDB** (local vector database)
- When you ask a question, it finds the **top 5 most relevant reviews**
- Passes them to **llama3.2** to generate an accurate answer
- Beautiful chat UI built with **Streamlit**

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| LangChain | LLM orchestration & RAG pipeline |
| Ollama | Run LLMs locally (llama3.2) |
| mxbai-embed-large | Embedding model |
| ChromaDB | Vector database |
| Streamlit | Web chat UI |
| Pandas | CSV data loading |

---

## 📁 Project Structure
