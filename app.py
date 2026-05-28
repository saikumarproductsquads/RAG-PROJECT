import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from vector import retriever

# --- Page Config ---
st.set_page_config(page_title="🍕 Pizza Restaurant Q&A", page_icon="🍕")
st.title("🍕 Pizza Restaurant Review Assistant")
st.write("Ask any question about the restaurant based on real customer reviews!")

# --- Prompt Template ---
template = """
You are an expert in answering questions about a pizza restaurant.
Don't make up any information. Use only the reviews provided to answer the question.
If you don't know the answer, say you don't know.

Here are some relevant reviews: {reviews}
Here is the question to answer: {question}
"""

# --- Load LLM (cached so it doesn't reload every time) ---
@st.cache_resource
def load_chain():
    llm = OllamaLLM(model="llama3.2")
    prompt = PromptTemplate.from_template(template)
    return prompt | llm

chain = load_chain()

# --- Chat History in Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display Previous Messages ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input ---
question = st.chat_input("Ask something about the pizza restaurant...")

if question:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Get answer
    with st.chat_message("assistant"):
        with st.spinner("Searching reviews and thinking..."):
            reviews = retriever.invoke(question)
            result = chain.invoke({"reviews": reviews, "question": question})
        st.markdown(result)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": result})