# Advanced Chunking and Document Preprocessing in RAG

## 1. Introduction to Chunking

In Retrieval-Augmented Generation (RAG), chunking is the process of dividing large documents into smaller, meaningful pieces before generating embeddings and storing them in a vector database.

A typical RAG pipeline looks like this:

```text
Documents
    |
    v
Document Loading
    |
    v
Preprocessing and Cleaning
    |
    v
Chunking
    |
    v
Embedding Generation
    |
    v
Vector Database
    |
    v
Retrieval
    |
    v
LLM Response
```

### Why Do We Need Chunking?

Imagine a Kubernetes document containing the following information:

- A Deployment manages ReplicaSets.
- A ReplicaSet maintains the desired number of Pods.
- A Pod runs one or more containers.

If we split this document at an arbitrary character limit, the definition of a ReplicaSet might be separated from its explanation.

Consequently, the retrieved chunk may not contain enough information to answer a question accurately.

Advanced chunking techniques aim to preserve:

- Semantic meaning
- Document structure
- Relationships between facts
- Contextual information
- Retrieval accuracy

**Key takeaway:** The objective of chunking is not simply to divide text into equal-sized pieces. It is to create useful, retrievable units of information.

---

## 2. Chunking Techniques

### 2.1 Fixed-Size Chunking

Fixed-size chunking divides text into chunks containing a predefined number of characters or tokens.

Example:

```text
Original Document
       |
       v
Chunk 1: First 500 tokens
Chunk 2: Next 500 tokens
Chunk 3: Next 500 tokens
```

**Advantages**

- Simple to implement
- Fast processing
- Predictable chunk sizes
- Useful as a baseline for experiments

**Disadvantages**

- May split sentences or paragraphs
- Can separate related information
- May produce incomplete context

**Use cases**

- Simple text documents
- Baseline RAG implementations
- Documents without meaningful structure

### 2.2 Recursive Character Chunking

Recursive character chunking attempts to split documents using progressively smaller separators.

A typical separator order is:

```text
Paragraphs
    |
    v
Newlines
    |
    v
Sentences or spaces
    |
    v
Characters
```

LangChain provides `RecursiveCharacterTextSplitter` for this purpose.

**Advantages**

- Attempts to preserve natural text boundaries
- Works well for general-purpose documents
- Easy to configure
- A strong baseline for RAG pipelines

**Disadvantages**

- Does not directly measure semantic similarity
- Can still separate related information
- Results depend on separators and size limits

**Use cases**

- Technical documentation
- Articles and reports
- General-purpose RAG applications

### 2.3 Semantic Chunking

Semantic chunking groups text based on meaning rather than relying only on fixed character limits.

It typically uses embeddings to identify changes in meaning between neighboring sentences or text units.

#### How Semantic Chunking Works

1. Split the document into sentences or small text units.
2. Generate an embedding for each sentence or unit.
3. Calculate similarity between neighboring embeddings.
4. Identify significant changes in semantic similarity.
5. Create chunk boundaries at suitable points.
6. Apply minimum and maximum chunk-size constraints.

Cosine similarity is commonly used to compare embeddings.

Formula:

```text
cosine_similarity(A, B) =
    (A . B) / (||A|| * ||B||)
```

Higher cosine similarity generally indicates that two vectors point in similar directions.

#### Example

Original text:

```text
Sentence 1: Kubernetes uses Pods as its smallest deployable units.

Sentence 2: A Pod can contain one or more containers.

Sentence 3: Horizontal Pod Autoscaler adjusts the number of replicas.

Sentence 4: Terraform uses declarative configuration files to manage infrastructure.
```

Possible semantic chunks:

```text
Chunk 1:
- Kubernetes Pods
- Containers
- Horizontal Pod Autoscaler

Chunk 2:
- Terraform
- Infrastructure as Code
```

The topic changes between Kubernetes and Terraform, so that boundary may be a good place to split.

**Advantages**

- Adapts chunk boundaries to the content
- Can preserve topic-level meaning
- Useful for documents containing multiple subjects

**Disadvantages**

- Requires embedding generation
- More computationally expensive than simple splitting
- Depends on the embedding model and similarity threshold
- Requires chunk-size constraints to avoid excessively small or large chunks

**Use cases**

- Research papers
- Long articles
- Knowledge bases
- Complex technical documentation

**Important:** Semantic chunking is not automatically better than recursive chunking. Its effectiveness should be evaluated against the target retrieval task.

### 2.4 Structure-Aware Chunking

Structure-aware chunking uses the document's existing organization to determine chunk boundaries.

Possible boundaries include:

- Headings and subheadings
- Paragraphs
- Markdown sections
- HTML elements
- Python functions and classes
- SQL statements
- YAML structures
- Table boundaries

Example:

```markdown
# Kubernetes

## Deployments

A Deployment manages ReplicaSets.

## Services

A Service exposes an application through a stable network endpoint.
```

A structure-aware splitter can preserve the relationship between each heading and its content.

**Advantages**

- Preserves document hierarchy
- Maintains meaningful section boundaries
- Works well for structured content

**Disadvantages**

- Requires appropriate parsing
- May create oversized chunks when sections are long
- Depends on the quality of the source structure

**Use cases**

- Technical documentation
- Markdown files
- API references
- Source code
- Product documentation

### 2.5 Parent-Child Chunking

Parent-child chunking separates retrieval granularity from the amount of context supplied to the LLM.

- **Child chunks:** Small pieces used for precise retrieval.
- **Parent chunks:** Larger sections containing additional context.

Example:

```text
Parent Chunk: Kubernetes Deployment Guide
    |
    |--- Child Chunk 1: Deployment definition
    |
    |--- Child Chunk 2: ReplicaSet behavior
    |
    |--- Child Chunk 3: Rolling updates
```

The system retrieves a relevant child chunk and then retrieves its associated parent section.

**Advantages**

- Improves retrieval granularity
- Provides additional context to the LLM
- Useful when a short fact depends on a larger explanation

**Disadvantages**

- Requires parent-child mapping
- Can increase context size
- Requires additional retrieval logic and storage

**Use cases**

- Large technical manuals
- Knowledge bases
- Long research documents

### 2.6 Sentence-Window Chunking

Sentence-window chunking uses a small text unit for retrieval while preserving surrounding sentences as context.

Example:

```text
Previous sentence
    |
Target sentence
    |
Next sentence
```

The target sentence may be embedded, while the surrounding sentences are stored or retrieved separately.

**Advantages**

- Supports precise matching
- Adds context around relevant sentences
- Useful for dense technical material

**Disadvantages**

- Requires additional context-management logic
- Context windows can contain irrelevant information
- Overlapping windows may introduce duplication

**Use cases**

- Research papers
- Technical manuals
- Documents containing short, precise facts

### 2.7 Sliding-Window Chunking

Sliding-window chunking creates overlapping chunks that move through a document.

Example:

```text
Chunk 1: Tokens 1-200
Chunk 2: Tokens 151-350
Chunk 3: Tokens 301-500
```

Here, each chunk contains 200 tokens, with 50 tokens of overlap.

Formula:

```text
Step Size = Chunk Size - Overlap
```

For a chunk size of 200 tokens and overlap of 50 tokens:

```text
Step Size = 200 - 50 = 150 tokens
```

**Advantages**

- Reduces information loss at chunk boundaries
- Preserves continuity
- Simple to implement

**Disadvantages**

- Increases storage and embedding costs
- Can produce duplicate retrieval results
- May increase the amount of redundant context

### 2.8 Proposition-Based Chunking

Proposition-based chunking transforms text into small, self-contained factual statements.

Example:

Original text:

```text
Kubernetes Deployments manage ReplicaSets, which maintain the desired
number of Pods.
```

Possible propositions:

```text
1. Kubernetes Deployments manage ReplicaSets.
2. ReplicaSets maintain the desired number of Pods.
```

An LLM may be used to identify or generate these propositions.

**Advantages**

- Supports fine-grained factual retrieval
- Can improve retrieval for specific questions
- Makes individual claims easier to identify

**Disadvantages**

- May require LLM processing
- Can increase preprocessing cost
- May lose relationships between facts
- Requires validation against the original source

**Use cases**

- Complex knowledge bases
- Fact-oriented question answering
- Dense technical documentation

### 2.9 LLM-Based Chunking

LLM-based chunking uses a language model to identify logical sections and boundaries.

Instead of relying entirely on fixed separators or embedding similarity, the model can consider document structure and meaning.

**Advantages**

- Handles complex, irregular documents
- Can identify logical sections
- Can support document-specific chunking policies

**Disadvantages**

- Higher computational cost
- Potentially slower preprocessing
- Boundaries may be inconsistent
- Requires validation and reproducible evaluation

### 2.10 Topic-Based Chunking

Topic-based chunking groups sentences or paragraphs that discuss the same subject.

It may use embeddings, clustering, topic models, or LLMs.

Example:

```text
Topic 1: Kubernetes networking
Topic 2: Kubernetes storage
Topic 3: Terraform infrastructure
```

**Advantages**

- Useful for multi-topic documents
- Can improve topic-level organization
- Helps separate unrelated discussions

**Disadvantages**

- Topic boundaries can be ambiguous
- Related topics may overlap
- Often requires additional computation

### 2.11 Code-Aware Chunking

Code-aware chunking respects programming-language syntax and logical boundaries.

Examples of useful boundaries:

- Functions
- Classes
- Modules
- Methods
- Syntax-tree nodes
- Configuration resources

For Python:

```python
def create_user(name):
    return {"name": name}


def delete_user(user_id):
    return {"deleted": user_id}
```

A code-aware splitter attempts to preserve complete functions rather than splitting them arbitrarily.

**Advantages**

- Preserves code structure
- Improves retrieval of implementation details
- Reduces broken or incomplete code snippets

**Use cases**

- Code assistants
- Repository question answering
- Terraform and Kubernetes configuration retrieval

### 2.12 Table-Aware Chunking

Table-aware chunking preserves relationships between table headers, rows, values, and units.

Example:

| Resource | CPU Request | Memory Request |
|---|---|---|
| API | 250m | 256Mi |
| Worker | 500m | 512Mi |

If a table is converted into unstructured text without preserving column associations, the retrieved values may become ambiguous.

**Best practices**

- Preserve column headers.
- Keep related rows together when possible.
- Retain units and captions.
- Store source and page metadata.
- Consider converting tables into structured records.

### 2.13 Contextual Chunking

Contextual chunking enriches an existing chunk with additional information about its source or surrounding document.

Example:

Original chunk:

```text
It supports automatic scaling based on resource utilization.
```

Context-enriched chunk:

```text
Document: Kubernetes Administration Guide
Section: Horizontal Pod Autoscaler

It supports automatic scaling based on resource utilization.
```

The added context makes the chunk easier to interpret independently.

**Advantages**

- Helps clarify otherwise ambiguous chunks
- Adds document and section context
- Can improve retrieval in large knowledge bases

**Disadvantages**

- Adds tokens and processing cost
- Can introduce errors if generated context is inaccurate
- Requires careful separation of original content and enrichment

### 2.14 Late Chunking

Late chunking changes when chunk embeddings are created.

In a traditional pipeline:

```text
Document
   |
   v
Split into chunks
   |
   v
Embed each chunk separately
```

In late chunking:

```text
Long document
   |
   v
Process the larger text with a long-context embedding model
   |
   v
Obtain token-level representations
   |
   v
Pool representations within each chunk boundary
   |
   v
Create chunk embeddings
```

This approach allows the representation of a chunk to reflect information from its broader context.

**Advantages**

- Can preserve contextual relationships across chunk boundaries
- Useful when isolated chunks are ambiguous

**Disadvantages**

- Requires a suitable embedding model and implementation
- Model context length can constrain processing
- Not supported by every embedding model

Late chunking is different from semantic chunking: semantic chunking chooses boundaries based on meaning, while late chunking changes how embeddings are constructed.

### 2.15 Agentic Chunking

Agentic chunking uses an LLM or agent to make document-specific chunking decisions.

An agent might classify the document and select a strategy:

```text
Input Document
      |
      v
Document Classification
      |
      v
Choose Chunking Strategy
      |
      +----> Prose: Recursive or semantic
      |
      +----> Code: Code-aware
      |
      +----> Tables: Table-aware
      |
      +----> Complex reports: Structure-aware or LLM-based
```

**Advantages**

- Adapts to different document types
- Can combine multiple chunking strategies
- Useful for heterogeneous document collections

**Disadvantages**

- Higher complexity and cost
- Requires validation of the chosen strategy
- Can produce inconsistent results without explicit rules

### 2.16 Multimodal Chunking

Multimodal chunking handles documents containing text, images, tables, diagrams, and other modalities.

Example:

```text
PDF Page
   |
   +----> Text
   |
   +----> Architecture Diagram
   |
   +----> Table
   |
   +----> Captions and Metadata
```

The pipeline should preserve relationships between the text and associated visual content.

**Use cases**

- Technical manuals
- Architecture documentation
- Research papers
- Presentation-based knowledge bases

---

## 3. Advanced Document Preprocessing

Preprocessing improves the quality of the source material before chunking and embedding.

### 3.1 Document Extraction

Extract content from:

- PDF
- DOCX
- HTML
- Markdown
- TXT
- CSV
- Excel
- Databases
- Source code

Scanned PDFs may require OCR to convert images of text into machine-readable content.

### 3.2 Text Cleaning and Normalization

Common operations include:

- Removing excessive whitespace
- Removing repeated headers and footers
- Removing irrelevant page numbers
- Repairing line breaks
- Removing unwanted HTML tags
- Normalizing Unicode when appropriate
- Fixing broken words caused by PDF extraction

Be careful not to damage source code, identifiers, punctuation, or mathematical expressions.

### 3.3 Deduplication

Deduplication identifies repeated content.

Two common approaches:

**Exact deduplication:** Removes identical documents or text blocks.

**Near-duplicate detection:** Identifies similar content despite minor formatting or wording differences.

Deduplication reduces redundant embeddings and prevents repeated content from dominating retrieval results.

### 3.4 Metadata Enrichment

Attach useful metadata to documents and chunks.

Example:

```python
metadata = {
    "source": "kubernetes-guide.pdf",
    "section": "Deployments",
    "page": 12,
    "document_type": "technical_document",
    "version": "1.2"
}
```

Useful metadata fields include:

- Source
- Document title
- Section
- Page number
- Version
- Creation or modification date
- Language
- Document type
- Access-control attributes

Metadata can support filtering, citations, debugging, and document version management.

### 3.5 Table and Layout Preservation

Tables should preserve:

- Column headers
- Row relationships
- Units
- Captions
- Page references

Do not blindly flatten complex tables into arbitrary strings. Use structured representations when appropriate.

### 3.6 Domain-Aware Processing

Different document types require different preprocessing strategies.

| Document Type | Recommended Processing |
|---|---|
| PDF | Extraction, layout preservation, optional OCR |
| Markdown | Heading-aware splitting |
| Python | Function- and class-aware splitting |
| YAML | Preserve indentation and resource boundaries |
| Logs | Preserve timestamps and event boundaries |
| CSV | Preserve headers and row structure |
| HTML | Remove boilerplate and preserve useful elements |
| Research papers | Preserve sections, citations, and tables |

### 3.7 Language Detection

Identify the language of the source document and choose appropriate tokenization and embedding approaches.

This is especially important for multilingual knowledge bases.

### 3.8 Quality and Security Checks

Check for:

- Empty or corrupted documents
- Invalid encodings
- Duplicate content
- Sensitive information
- Untrusted instructions embedded in source documents
- Documents that users are not authorized to access

Preserve source permissions and enforce access controls during retrieval. Merely storing access-control metadata does not enforce authorization.

---

## 4. Chunk Size and Overlap

There is no universally optimal chunk size.

The best configuration depends on:

- Document structure
- Embedding model
- Query type
- Retrieval method
- Available context window
- Accuracy and latency requirements

### Small Chunks

**Advantages**

- More precise retrieval
- Less irrelevant content

**Disadvantages**

- May lose surrounding context
- May separate related facts

### Large Chunks

**Advantages**

- Preserve more context
- Can contain complete explanations

**Disadvantages**

- May reduce retrieval precision
- Can introduce irrelevant information
- Consume more context-window tokens

### Overlapping Chunks

Overlap preserves some content between adjacent chunks.

Formula:

```text
Step Size = Chunk Size - Overlap
```

Example:

```text
Chunk Size = 200 tokens
Overlap = 50 tokens

Step Size = 200 - 50 = 150 tokens
```

Overlap can help preserve continuity, but excessive overlap increases redundancy and storage costs.

### Experimental Starting Points

These are illustrative values for experimentation, not universal recommendations.

| Strategy | Starting Configuration |
|---|---|
| Recursive baseline | 500 tokens, 50-token overlap |
| Small chunks | 150–250 tokens |
| Large chunks | 800–1,000 tokens |
| Semantic chunking | Experiment with similarity thresholds and size limits |

Verify whether the splitter measures characters or tokens before comparing chunk sizes.

---

## 5. Evaluating Chunking Quality

Chunk quality should be evaluated using retrieval performance, not just visual inspection.

### Retrieval Metrics

**Recall@k**

Measures whether relevant chunks appear among the top `k` retrieved results.

**Precision@k**

Measures how many of the top `k` retrieved results are relevant.

**MRR — Mean Reciprocal Rank**

Measures how highly the first relevant result appears in the ranking.

### Answer Metrics

**Faithfulness:** Measures whether the generated answer is supported by the retrieved context.

**Answer correctness:** Measures whether the answer is correct against an appropriate reference.

### Operational Metrics

- Indexing time
- Embedding cost
- Retrieval latency
- Storage requirements
- Number of chunks
- Duplicate retrieval rate

### Recommended Experiment

1. Prepare a fixed collection of documents.
2. Create 10–20 questions with known supporting passages.
3. Apply fixed-size, recursive, and semantic chunking.
4. Use the same embedding model and vector database.
5. Keep retrieval settings consistent.
6. Compare Recall@k, Precision@k, answer quality, and cost.

This provides a fair comparison of chunking strategies.

---

## 6. Recommended Practical Demonstration

For a hands-on RAG lesson, follow this order:

1. Load a technical document.
2. Inspect the raw extracted text.
3. Clean the text and preserve metadata.
4. Demonstrate fixed-size chunking.
5. Demonstrate recursive character chunking.
6. Implement semantic chunking.
7. Compare chunk boundaries and sizes.
8. Demonstrate structure-aware chunking.
9. Explain parent-child retrieval.
10. Store chunks in a vector database.
11. Ask the same questions against each configuration.
12. Compare retrieval results and answer quality.

### Suggested Demo Dataset

Use a small technical knowledge base containing:

- Kubernetes deployment documentation
- Terraform resource examples
- Troubleshooting guides
- A table containing resource limits

This allows you to compare how different techniques handle prose, code, and structured data.

---

## 7. Common Mistakes

1. Assuming semantic chunking is always better than recursive chunking.
2. Choosing chunk sizes without considering the retrieval task.
3. Removing headings and metadata during preprocessing.
4. Using excessive overlap.
5. Applying generic text splitting to code and YAML.
6. Comparing strategies with different embedding models or retrieval configurations.
7. Evaluating chunk readability without measuring retrieval quality.
8. Treating contextual enrichment as a substitute for accurate citations.
9. Ignoring access control when retrieving sensitive documents.
10. Assuming every advanced chunking technique is supported by every framework.

Avoid blindly removing stop words, stemming all text, or lowercasing everything. These transformations can damage technical terminology, identifiers, negation, and code.

---

## 8. Final Comparison

| Technique | Main Advantage | Complexity |
|---|---|---|
| Fixed-size | Simple baseline | Low |
| Recursive | Preserves natural boundaries where possible | Low |
| Semantic | Adapts boundaries to changes in meaning | Medium–High |
| Structure-aware | Preserves document organization | Low–Medium |
| Parent-child | Precise retrieval with broader context | Medium |
| Sentence-window | Adds neighboring context | Medium |
| Proposition-based | Fine-grained factual retrieval | High |
| Contextual chunking | Adds useful document context | Medium–High |
| Late chunking | Uses broader context in chunk representations | High |
| Agentic chunking | Adapts strategy to document type | High |
| Multimodal chunking | Preserves relationships across modalities | High |

---

## 9. Recommended Learning Path

For a practical GenAI/RAG course, prioritize the following techniques for coding demonstrations:

1. **Preprocessing:** Cleaning, deduplication, and metadata.
2. **Recursive chunking:** Establish a baseline.
3. **Semantic chunking:** Explore meaning-based boundaries.
4. **Structure-aware chunking:** Preserve headings, code, and tables.
5. **Parent-child retrieval:** Balance precise matching with context.
6. **Evaluation:** Compare retrieval quality using a fixed test set.

Introduce proposition-based chunking, contextual chunking, late chunking, and agentic chunking as advanced concepts.

## 10. Key Takeaway

A high-quality RAG pipeline requires more than a good embedding model or vector database.

The overall process should preserve meaningful content, choose appropriate chunk boundaries, retain useful metadata, and retrieve the right context for each question.

**The best chunking strategy is the one that produces the most accurate, relevant, and cost-effective retrieval results for your specific use case.**
