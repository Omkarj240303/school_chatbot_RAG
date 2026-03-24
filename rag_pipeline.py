from dotenv import load_dotenv
import os

from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

#  Load env
load_dotenv()

# Load data
with open("data/SDV_data_new.txt") as f:
    files = f.read()

# Split
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=250
)

texts = text_splitter.create_documents([files])

# Embeddings
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

# Vector DB
vector_db = Chroma(
    collection_name="Omkar",
    embedding_function=embeddings_model,
    persist_directory="db"
)

# Add documents to vector DB if not already present
if not vector_db.get()['ids']:
    vector_db.add_documents(texts)

retriever = vector_db.as_retriever()

# LLM
llm = ChatOpenAI(model="gpt-4.1-nano")

#Prompt
template = """Use the context provided to answer the query.
If you don't know, say I don't know.

context: {context}
query: {query}
Answer:"""

prompt = PromptTemplate.from_template(template)

#Chain
rag_chain = (
    {"context": retriever, "query": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Function to get answer
def get_answer(question: str):
    return rag_chain.invoke(question)
