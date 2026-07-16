from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os


load_dotenv()

llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL"),
    base_url=os.getenv("OLLAMA_BASE_URL"),
)

embeddings = OllamaEmbeddings(
    model=os.getenv("EMBEDDING_MODEL"),
    base_url=os.getenv("OLLAMA_BASE_URL"),
)