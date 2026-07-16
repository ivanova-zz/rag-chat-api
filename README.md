# RAG Chat with FastAPI, Ollama and ChromaDB

A Retrieval-Augmented Generation (RAG) chatbot built with **FastAPI**, **LangChain**, **Ollama**, and **ChromaDB**.

The application ingests PDF and Markdown documents, stores their embeddings in a Chroma vector database, and answers user questions using a locally running LLM through Ollama.

## Features

- REST API built with FastAPI
- Document ingestion (PDF and Markdown)
- Vector search with ChromaDB
- Local LLM inference using Ollama
- Docker Compose deployment
- No external AI APIs required
- Modular project structure

## Tech Stack

- Python 3.12
- FastAPI
- LangChain
- Ollama
- ChromaDB
- Docker & Docker Compose

## Project Structure

```text
rag-chat/
├── app/
│   ├── config.py
│   ├── ingest.py
│   ├── main.py
│   ├── rag.py
│   └── prompts.py
├── knowledge/
│   ├── docs.pdf
│   ├── faq.pdf
│   └── seo.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run_ingest.py
├── .env.example
└── README.md
```

## Architecture

```
                 +--------------------+
                 |      FastAPI       |
                 |   /chat /ingest    |
                 +---------+----------+
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
   +---------------+               +----------------+
   |    Ollama     |               |    ChromaDB    |
   | LLM + Embeds  |               | Vector Store   |
   +---------------+               +----------------+
                  ^
                  |
             Knowledge Base
           PDF / Markdown Files
```

## Prerequisites

- Docker
- Docker Compose

## Environment Variables

Create a `.env` file from `.env.example`.

Example:

```env
OLLAMA_BASE_URL=http://ollama:11434

OLLAMA_MODEL=llama3.1
EMBEDDING_MODEL=nomic-embed-text

CHROMA_HOST=chroma
CHROMA_PORT=8000

COLLECTION_NAME=knowledge
```

## Installation

Clone the repository.

```bash
git clone <repository-url>

cd rag-chat
```

Build and start the containers.

```bash
docker compose up -d --build
```

## Download Ollama Models

After the containers are running:

```bash
docker exec -it ollama ollama pull llama3.1
```

```bash
docker exec -it ollama ollama pull nomic-embed-text
```

Verify:

```bash
docker exec -it ollama ollama list
```

## Ingest Documents

Place your documents inside the `knowledge/` directory.

Run:

```bash
docker compose exec api python run_ingest.py
```

This will:

- load PDF and Markdown documents
- split them into chunks
- generate embeddings
- store them in ChromaDB

## Run the API

The API will be available at:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

## API Endpoints

### POST /ingest

Indexes documents from the knowledge directory.

### POST /chat

Example request:

```json
{
  "question": "How does SEO optimization work?"
}
```

Example response:

```json
{
  "answer": "SEO optimization improves website visibility in search engines..."
}
```

## Future Improvements

- Conversation memory
- Streaming responses
- Multi-user support
- Authentication
- Hybrid search
- Reranking
- Source citations
- File upload endpoint
- Redis caching
- Kubernetes deployment

## License

MIT