# Foundations Required Before Building RAG Systems

## 1. Why LLMs Need External Knowledge
Large Language Models (LLMs) are trained
on static datasets and do not have real-time
or private knowledge.

Limitations of LLMs:
- Hallucinations
- Outdated information
- No access to private data
- High cost if retrained

This is where RAG is required.

---

## 2. Difference Between RAG and Fine-Tuning

### RAG
- Retrieves external documents
- No model retraining
- Faster and cheaper
- Easy to update knowledge

### Fine-Tuning
- Updates model weights
- Expensive and time-consuming
- Risk of overfitting
- Used for behavior/style changes

---

## 3. Understanding Embeddings
Embeddings are numerical representations
of text that capture semantic meaning.

Similar text → similar vectors

Used for:
- Semantic search
- Question answering
- Clustering

---

## 4. Vector Databases
Vector databases store embeddings and
enable fast similarity search.

Common examples:
- FAISS
- Chroma
- Pinecone
- Weaviate

---

## 5. Retrieval vs Generation

### Retrieval
- Finds relevant information
- Uses similarity search
- No text generation

### Generation
- Produces natural language answers
- Uses LLM
- Depends on retrieved context

RAG combines both.

---

## 6. Chunking Strategy
Documents must be split into smaller
chunks before embedding.

Reasons:
- Token limits
- Better retrieval accuracy
- Faster search

---

## 7. Context Window Limitation
LLMs can only process a limited number
of tokens at a time.

RAG helps by sending only
relevant context to the model.

---

## 8. Cost Considerations in RAG
Costs mainly come from:
- Embedding generation
- LLM API calls

RAG reduces cost by:
- Reusing embeddings
- Avoiding retraining

---

## 9. When NOT to Use RAG
- Small datasets
- Simple FAQs
- When data rarely changes

---

## Summary
RAG is a system design approach
that enhances LLMs with external knowledge
without retraining the model.
