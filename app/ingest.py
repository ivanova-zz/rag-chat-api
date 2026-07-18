from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import embeddings
import os
import chromadb
from langchain_chroma import Chroma


KNOWLEDGE_DIR = Path("knowledge")
CHROMA_DIR = "chroma_db"


def ingest_documents():
    documents = []

    # Загружаем все документы
    for file in KNOWLEDGE_DIR.iterdir():

        if file.suffix == ".pdf":
            loader = PyPDFLoader(str(file))
            documents.extend(loader.load())

        elif file.suffix == ".md":
            loader = TextLoader(str(file), encoding="utf-8")
            documents.extend(loader.load())

    print(f"Loaded {len(documents)} documents")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    client = chromadb.HttpClient(
        host=os.getenv("CHROMA_HOST"),
        port=int(os.getenv("CHROMA_PORT")),
    )

    db = Chroma(
        client=client,
        collection_name=os.getenv("COLLECTION_NAME"),
        embedding_function=embeddings,
    )

    db.add_documents(chunks)

    print("Documents indexed successfully.")