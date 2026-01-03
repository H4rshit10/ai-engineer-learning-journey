# Retrieval-Augmented Generation (RAG)

## What is RAG?
Retrieval-Augmented Generation (RAG) is an approach that enhances
Large Language Models (LLMs) by retrieving relevant external
information before generating a response.

Instead of relying only on the model’s internal knowledge,
RAG fetches updated and relevant data from external sources.

---

## Why RAG is needed
- LLMs have limited and static knowledge
- Reduces hallucinations
- Allows use of private or domain-specific data
- No need to retrain the model

---

## RAG Workflow
1. User query is received
2. Query is converted into embeddings
3. Relevant data is retrieved from a vector database
4. Retrieved context is added to the prompt
5. LLM generates a grounded response

---

## Key Components
- Data source
- Chunking
- Embedding model
- Vector database
- Retriever
- Prompt construction
- Large Language Model (LLM)

---

## When to use RAG
- Question answering over documents
- Chatbots with custom knowledge
- Search-based AI applications
- Enterprise knowledge systems

---

## Notes
This document contains conceptual understanding of RAG.
Implementation and code will be added later.
