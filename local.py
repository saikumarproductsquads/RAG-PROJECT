
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from vector import retriever
# Step 2: Create a prompt template( nothing but instructions to llm)
template = """
You are an expert in answering questions about a pizza restaurant.
Don't make up any information. Use only the reviews provided to answer the question.
dont go for the hallucination. if you dont know the answer, say you dont know. 
Here are some relevant reviews: {reviews}
Here is the question to answer: {question}
"""

# Step 3: Initialize the Ollama LLM
llm = OllamaLLM(model="llama3.2")

# Step 4: Format the prompt
prompt = PromptTemplate.from_template(template)
chain = prompt | llm

# step 5: use the while loop to continuosly ask questions
while True:
    print("\n"+"-----------")
    question = input("ask a question about the pizza restaurantst: ")
    if question.lower() == "stop":
        break
# Step 6: Send prompt to the model
    reviews = retriever.invoke(question)
    result = chain.invoke({
    "reviews": reviews, 
    "question": question
    })

# Step 6: Print the response
    print("\n"+"-----------")
    print(result)
  

