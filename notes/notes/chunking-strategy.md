# Chunking Strategy in RAG Systems

## What is Chunking?
Chunking is the process of splitting
large documents into smaller pieces
before generating embeddings.

LLMs and vector databases work best
with smaller, meaningful chunks.

---

## Why Chunking is Important
- LLMs have token limits
- Improves retrieval accuracy
- Reduces irrelevant context
- Optimizes cost and performance

---

## Chunk Size
Chunk size refers to how much text
is included in one chunk.

### Small Chunks
Pros:
- More precise retrieval
- Less noise

Cons:
- Loss of context
- More embeddings (higher cost)

### Large Chunks
Pros:
- Better context
- Fewer embeddings

Cons:
- Less precise retrieval
- More irrelevant information

---

## Chunk Overlap
Chunk overlap means repeating
a portion of text between chunks.

### Why Overlap is Needed
- Prevents loss of meaning
- Maintains continuity
- Improves answer quality

Common overlap: 10% – 20%

---

## Types of Chunking

### 1. Fixed-Length Chunking
Splits text by character or token count.

Simple but may break meaning.

---

### 2. Sentence-Based Chunking
Splits by sentences.

Better semantic integrity.

---

### 3. Paragraph-Based Chunking
Uses paragraphs as chunks.

Best for structured documents.

---

### 4. Semantic Chunking
Splits text based on meaning.

Most accurate but complex.

---

## Chunking in RAG Pipeline
1. Load documents
2. Split into chunks
3. Generate embeddings
4. Store in vector database
5. Retrieve relevant chunks

---

## Common Chunking Mistakes
- Too large chunks
- No overlap
- Breaking mid-sentence
- Ignoring document structure

---

## Best Practices
- Start with 300–500 tokens
- Use 10–20% overlap
- Adjust based on use case
- Evaluate retrieval quality

---

## Summary
Chunking directly impacts
retrieval accuracy and
LLM response quality.
