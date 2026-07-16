from langchain_chroma import Chroma

from app.config import embeddings, llm
from app.prompts import RAG_PROMPT
import os

db = Chroma(
    collection_name=os.getenv("COLLECTION_NAME"),
    host=os.getenv("CHROMA_HOST"),
    port=int(os.getenv("CHROMA_PORT")),
    embedding_function=embeddings,
)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)


def ask(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        d.page_content for d in docs
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question,
    )

    response = llm.invoke(prompt)

    return response.content