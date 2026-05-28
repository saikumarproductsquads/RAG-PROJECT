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

```
RAG-PROJECT/
│
├── app.py                              # Streamlit chat UI
├── vector.py                           # Embeddings & ChromaDB setup
├── realistic_restaurant_reviews.csv    # Customer reviews dataset
├── requirements.txt                    # All dependencies
├── README.md                           # Project documentation
└── chroma_db/                          # Auto-generated vector store
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed

### 1. Clone the Repository
```bash
git clone https://github.com/saikumarproductsquads/RAG-PROJECT.git
cd RAG-PROJECT
```

### 2. Create Virtual Environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Pull Ollama Models
```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

### 5. Start Ollama Server
```bash
ollama serve
```

### 6. Run the App
```bash
streamlit run app.py
```

Open your browser at 👉 `http://localhost:8501`

---

## 💬 How It Works

```
User Question
      ↓
Convert question to vector (mxbai-embed-large)
      ↓
Search ChromaDB → Top 5 relevant reviews
      ↓
Send reviews + question to llama3.2
      ↓
Answer based only on real reviews ✅
```

---

## 🖥️ Screenshots

> App running at localhost:8501

![App Screenshot](screenshot.png)

---

## 📦 Requirements

```
langchain
langchain-ollama
langchain-chroma
streamlit
pandas
chromadb
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🚀 Key Features

- ✅ 100% Local — No API keys needed
- ✅ No hallucination — Answers only from real reviews
- ✅ Chat history maintained during session
- ✅ Fast retrieval using ChromaDB vector search
- ✅ Clean and simple Streamlit UI

---

## 👨‍💻 Author

**Sai Kumar Bellala**  
GitHub: [@saikumarproductsquads](https://github.com/saikumarproductsquads)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
```

---

## How to Add This to Your Project

**Step 1:** Create `README.md` in your project folder and paste the above content.

**Step 2:** Push it to GitHub:
```powershell
git add README.md
git commit -m "added README"
git push
```

