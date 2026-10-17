# NLP and TF-IDF

## 1. What is NLP?

**NLP stands for Natural Language Processing.**

NLP is a field of Artificial Intelligence (AI) that enables computers to process, analyze, understand, and generate human language, such as English or Kannada.

For example, humans can read the sentence:

> I love learning Python.

We understand its meaning naturally. A computer initially sees text as a sequence of characters. NLP techniques help computers process that text and perform useful tasks.

### Why do we need NLP?

NLP helps computers work with the huge amount of unstructured text that humans create.

Examples:

- **Chatbots:** Understand user questions and generate answers.
- **Search engines:** Find relevant information from a query.
- **Sentiment analysis:** Identify whether a review is positive or negative.
- **Translation:** Translate Kannada into English.
- **Spam detection:** Identify unwanted emails.
- **RAG applications:** Retrieve relevant documents before an LLM generates an answer.
- **Voice assistants:** Process speech after it has been converted into text.

### AI vs. ML vs. NLP vs. GenAI

- **Artificial Intelligence (AI):** The broad field of building intelligent systems.
- **Machine Learning (ML):** A field where systems learn patterns from data.
- **NLP:** Techniques for processing human language; NLP can use ML and deep learning.
- **Generative AI:** AI systems that generate new content, such as text, images, or code.

These areas overlap. NLP is not limited to traditional machine learning, and modern LLMs combine language processing with generative capabilities.

---

## 2. How does NLP process text?

Imagine we have this sentence:

`I am learning Natural Language Processing`

An NLP pipeline might process it through these stages:

1. **Raw text:** `I am learning Natural Language Processing`
2. **Tokenization:** Split the sentence into smaller units.
3. **Text normalization:** Standardize text where appropriate.
4. **Numerical representation:** Convert text into numbers or vectors.
5. **Model or algorithm:** Classify, search, summarize, or generate text.

These stages are not mandatory in every NLP application. Modern transformer models use their own tokenizers and learned representations rather than requiring every traditional preprocessing step.

---

## 3. Important NLP techniques

NLP has several techniques. Each technique solves a different problem.

| Technique | What it does | Example |
|---|---|---|
| Tokenization | Splits text into tokens | `"I love Python"` → `["I", "love", "Python"]` |
| Stop-word removal | Removes selected common words | `"the cat is sleeping"` → `"cat sleeping"` |
| Stemming | Reduces words to approximate roots | `"playing"` → `"play"` |
| Lemmatization | Converts words to dictionary forms | `"better"` → `"good"` in the appropriate context |
| Bag of Words (BoW) | Represents text using word counts | `"Python Python AI"` → counts for each word |
| TF-IDF | Weights words based on frequency and rarity across documents | A distinctive term gets more weight than a common term |
| N-grams | Captures sequences of words or tokens | `"machine learning"` as a bigram |
| Word embeddings | Represents words or text as dense numerical vectors | `"king"` and `"queen"` may have related representations |
| POS tagging | Identifies grammatical roles | `"run"` → verb in `"I run daily"` |
| Named Entity Recognition (NER) | Identifies names, places, organizations, etc. | `"Google"` → organization |
| Sentiment analysis | Estimates emotional polarity | `"The movie was excellent"` → positive |
| Transformer-based processing | Learns contextual relationships in text | BERT, GPT |

**Teaching tip:** Start with tokenization, Bag of Words, and TF-IDF before moving to embeddings. Students will then understand why modern semantic search differs from traditional keyword-based methods.

---

## 4. What is TF-IDF?

**TF-IDF stands for Term Frequency–Inverse Document Frequency.**

It is a traditional NLP technique that assigns a numerical importance score to a word within a document relative to a collection of documents.

The central idea:

- A word appearing frequently in one document may be important to that document.
- A word appearing in almost every document is less useful for distinguishing one document from another.

For example, words like `the`, `is`, and `and` are common in English. A term like `Kubernetes` may be much more useful for identifying a document about Kubernetes.

TF-IDF helps represent documents numerically, identify distinctive terms, and build keyword-search or text-classification systems.

### 4.1 TF — Term Frequency

Term Frequency measures how frequently a term appears in a document.

\[
TF(t,d)=\frac{\text{Count of term }t\text{ in }d}{\text{Total terms in }d}
\]

A term that occurs more often in a document generally receives a higher TF score.

### 4.2 IDF — Inverse Document Frequency

Inverse Document Frequency measures how rare a term is across the entire document collection.

\[
IDF(t)=\ln\left(\frac{N}{DF(t)}\right)
\]

Where:

- \(N\): Total number of documents.
- \(DF(t)\): Number of documents containing term \(t\).
- \(\ln\): Natural logarithm.

A term found in fewer documents receives a higher IDF score under this formula.

### 4.3 TF-IDF formula

\[
TF\text{-}IDF(t,d)=TF(t,d)\times IDF(t)
\]

A term receives a high score when it occurs frequently in a particular document but is relatively rare across the collection.

> **Note:** Different libraries use different TF-IDF variants, smoothing methods, and normalization settings. The equations above illustrate the basic concept.

---

## 5. TF-IDF example — Calculate it step by step

Suppose we have three documents:

- **D1:** `Python is easy. Python is powerful.`
- **D2:** `Python is popular.`
- **D3:** `Java is powerful.`

Let's calculate the TF-IDF score of the word **Python in document D1**.

### Step 1: Calculate TF

D1 contains 6 words:

`Python, is, easy, Python, is, powerful`

Python appears twice.

\[
TF(\text{Python},D1)=\frac{2}{6}=0.3333
\]

### Step 2: Calculate IDF

Python appears in D1 and D2, so it occurs in 2 out of 3 documents.

\[
IDF(\text{Python})=\ln\left(\frac{3}{2}\right)
\]

\[
IDF(\text{Python})\approx 0.4055
\]

### Step 3: Calculate TF-IDF

\[
TF\text{-}IDF=0.3333\times0.4055
\]

\[
\boxed{TF\text{-}IDF\approx0.1352}
\]

This score measures how distinctive the word `Python` is in D1 under our chosen formula.

### What happens to the word `is`?

The word `is` appears in all three documents.

\[
IDF(\text{is})=\ln\left(\frac{3}{3}\right)=0
\]

Therefore, its TF-IDF score is zero under this unsmoothed formula.

This illustrates the key concept: **a word appearing in every document does not help distinguish one document from another.**

---

## 6. How does TF-IDF create a sparse matrix?

Connect this concept to dense and sparse vectors.

Suppose we have two documents:

- **D1:** `Python is easy`
- **D2:** `Java is powerful`

After tokenization, the vocabulary could be:

`["easy", "is", "java", "powerful", "python"]`

Bag of Words represents each document using word counts. TF-IDF replaces those counts with importance scores.

An illustrative TF-IDF matrix might look like this:

| Document | easy | is | java | powerful | python |
|---|---:|---:|---:|---:|---:|
| D1 | 0.70 | 0.00 | 0.00 | 0.00 | 0.70 |
| D2 | 0.00 | 0.00 | 0.70 | 0.70 | 0.00 |

These values are illustrative, not exact outputs from a particular TF-IDF implementation.

Notice that most entries are zero. This is a **sparse matrix**.

TF-IDF commonly produces sparse vectors because each document contains only a small portion of the vocabulary.

---

## 7. Implement TF-IDF in Python

This example uses scikit-learn.

### Install the library

```bash
pip install scikit-learn
```

### Cell 1 — Import the library

```python
from sklearn.feature_extraction.text import TfidfVectorizer
```

### Cell 2 — Create sample documents

```python
documents = [
    "Python is easy. Python is powerful.",
    "Python is popular.",
    "Java is powerful."
]
```

### Cell 3 — Create the TF-IDF vectorizer

```python
vectorizer = TfidfVectorizer()
```

The vectorizer tokenizes the text, builds a vocabulary, calculates TF-IDF weights, and normally applies L2 normalization to the resulting document vectors.

### Cell 4 — Convert text into numerical vectors

```python
tfidf_matrix = vectorizer.fit_transform(documents)

print(tfidf_matrix)
```

The result is a sparse matrix rather than a regular, fully populated NumPy array.

### Cell 5 — Print the vocabulary

```python
words = vectorizer.get_feature_names_out()

print(words)
```

This shows the terms used as the matrix columns.

### Cell 6 — Display the complete matrix

```python
matrix = tfidf_matrix.toarray()

print(matrix)
```

`.toarray()` converts the sparse matrix into a dense NumPy array for learning and visualization. For large datasets, avoid doing this unnecessarily because it can consume a lot of memory.

### Cell 7 — Display the matrix with column names

```python
for i, row in enumerate(matrix):
    print(f"\nDocument {i + 1}")

    for j, word in enumerate(words):
        print(f"{word}: {row[j]:.4f}")
```

This helps students see the numerical weight assigned to each word in each document.

---

## 8. TF-IDF vs. word embeddings

This is particularly important when teaching RAG.

| Feature | TF-IDF | Dense embeddings |
|---|---|---|
| Representation | Sparse vector | Dense vector |
| Main signal | Word frequency and document rarity | Learned semantic and contextual patterns |
| Understands synonyms | Not inherently | Often captures semantic relationships |
| Exact technical terms | Often effective | Depends on the model |
| Example techniques | TF-IDF, BM25 | Sentence Transformers, OpenAI embeddings |
| Typical retrieval | Keyword-based | Semantic search |

Imagine a document says:

`The server is experiencing high CPU utilization.`

A student searches:

`Why is my processor overloaded?`

TF-IDF may struggle because the query and document use different words. A good embedding model may recognize that the phrases are semantically related.

This is why modern RAG systems often use **dense retrieval, sparse retrieval, or hybrid search**, depending on their requirements.

---

## 9. Quick revision notes

- **NLP:** Techniques that enable computers to process human language.
- **Tokenization:** Splits text into tokens.
- **Bag of Words:** Represents documents using word counts.
- **TF-IDF:** Assigns word-importance weights using term frequency and inverse document frequency.
- **Sparse matrix:** A matrix containing mostly zero values.
- **Dense embeddings:** Numerical representations designed to capture semantic information.
- **BM25:** A ranking algorithm widely used for keyword-based information retrieval.
- **Hybrid search:** Combines keyword retrieval and semantic retrieval.

## 10. Recommended learning sequence

1. NLP introduction
2. Text preprocessing
3. Bag of Words
4. TF-IDF
5. BM25
6. Word embeddings
7. Cosine similarity
8. Dense and sparse retrieval
9. Hybrid search
10. Retrieval-Augmented Generation (RAG)

This sequence takes students from traditional NLP to modern GenAI retrieval systems step by step.
