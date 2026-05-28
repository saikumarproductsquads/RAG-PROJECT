from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd
import os

# step 1 : import the csv file 
df = pd.read_csv("realistic_restaurant_reviews.csv")
df.columns = df.columns.str.strip()  # ADD THIS LINE
# step 2 : import the embeddings model 
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
# step 3 : store of vectore data base
db_location="./chroma_db"
# step 4 : chunk the data and create vectors in db
add_documents = not os.path.exists(db_location)
if add_documents:
    documents = []
    ids  = []
    for i,row in df.iterrows() :
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row['Rating'], "date": row['Date']},
            id=str(i)
        )
        documents.append(document)
        ids.append(str(i))
# intialising vector store
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
# retrive
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)