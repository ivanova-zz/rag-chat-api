RAG_PROMPT = """
You are an assistant.

Answer ONLY using the provided context.

If the answer is not in the context, reply:

"I don't know."

Context:

{context}

Question:

{question}
"""