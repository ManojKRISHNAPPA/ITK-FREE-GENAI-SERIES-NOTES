# Transformer: Encoder and Decoder

## 1. Why do we need an Encoder and Decoder?

Consider a simple translation task:

**Input:**

> I love India

**Expected Output:**

> ನಾನು ಭಾರತವನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ

The Transformer needs to perform two major tasks:

1. Understand the input sentence.
2. Generate the output sentence.

The **Encoder** is mainly responsible for understanding the input, while the **Decoder** is responsible for generating the output.

A simple way to remember this is:

```text
Encoder  → Understand the input
Decoder  → Generate the output
```

---

# 2. High-Level Transformer Architecture

The original Transformer architecture contains two major components:

```text
                         TRANSFORMER
                              |
              +---------------+---------------+
              |                               |
           ENCODER                         DECODER
              |                               |
        Understand input                Generate output
              |                               |
              +---------------+---------------+
                              |
                           OUTPUT
```

For example:

```text
Input:
"I love India"

        |
        v

     ENCODER
        |
        | Contextual representation
        v

     DECODER
        |
        | Generates one token at a time
        v

"ನಾನು ಭಾರತವನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ"
```

---

# 3. What is Encoding?

Encoding is the process of converting the input sentence into a representation that captures the meaning and context of the sentence.

For example:

```text
"I love India"
```

The Encoder processes all the input tokens and creates **contextual representations**.

The important point is:

> The Encoder does not directly produce the translated sentence.

Instead, it produces information that the Decoder can use to generate the output.

---

# 4. Step 1: Tokenization

Before the Encoder processes the sentence, the text is converted into tokens.

For example:

```text
"I love India"
```

can be represented as:

```text
["I", "love", "India"]
```

Each token is then converted into a numerical representation.

```text
"I"      → Token
"love"   → Token
"India"  → Token
```

---

# 5. Step 2: Token Embeddings

Neural networks cannot directly understand words such as:

```text
"I"
"love"
"India"
```

Therefore, each token is converted into a numerical vector called an **embedding**.

Conceptually:

```text
"I"      → [0.12, 0.45, 0.76, ...]
"love"   → [0.32, 0.11, 0.89, ...]
"India"  → [0.91, 0.22, 0.34, ...]
```

These numbers are learned representations.

The actual embedding values are much larger vectors in real Transformer models.

---

# 6. Step 3: Positional Encoding

A Transformer processes tokens in parallel.

Therefore, the model needs some way to understand the position of each token.

For example:

```text
I       → Position 1
love    → Position 2
India   → Position 3
```

Positional information is added to the token embeddings.

```text
Token Embedding
       +
Positional Encoding
       |
       v
Input Representation
```

This helps the model distinguish between different word orders.

For example:

```text
"I love India"

and

"India love I"
```

contain the same words but have completely different meanings.

---

# 7. Step 4: Encoder Self-Attention

The most important component of the Encoder is **Self-Attention**.

Self-attention allows each token to look at other tokens in the same input sentence and understand their relationships.

Consider:

```text
"I love India"
```

The word `love` can be related to both `I` and `India`.

Conceptually:

```text
       I
       ↕
      love
       ↕
     India
```

The model calculates how important each token is to another token.

This helps the model build a contextual understanding of the sentence.

---

# 8. Q, K and V in Self-Attention

Self-attention uses three important concepts:

```text
Q → Query
K → Key
V → Value
```

A simple analogy is:

* **Query** → What information am I looking for?
* **Key** → What information do I contain?
* **Value** → What information should I provide?

The attention mechanism calculates how strongly a Query should attend to different Keys and then uses the corresponding Values.

The simplified formula is:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

You do not need to memorize the formula initially.

The important idea is:

```text
Query + Keys
      |
      v
Attention Scores
      |
      v
Weighted Values
      |
      v
Contextual Representation
```

---

# 9. What does the Encoder finally produce?

After passing through the Encoder layers, we get contextual representations of the input.

Conceptually:

```text
"I"      → Context-aware representation
"love"   → Context-aware representation
"India"  → Context-aware representation
```

These representations contain information about the input sentence.

We can think of the Encoder output as:

```text
Input Sentence
      |
      v
Encoder
      |
      v
Contextual Representations
```

These representations are passed to the Decoder.

---

# 10. What is Decoding?

Decoding is the process of generating the output sequence using:

1. The information produced by the Encoder.
2. The tokens generated by the Decoder so far.

For example:

```text
Input:

"I love India"

        |
        v

     Encoder

        |
        v

Contextual representation

        |
        v

     Decoder

        |
        v

"ನಾನು"
```

The Decoder then continues generating the next token.

```text
<START> → ನಾನು
```

Then:

```text
<START> → ನಾನು → ಭಾರತವನ್ನು
```

Then:

```text
<START> → ನಾನು → ಭಾರತವನ್ನು → ಪ್ರೀತಿಸುತ್ತೇನೆ
```

Finally:

```text
<START>
   ↓
ನಾನು
   ↓
ಭಾರತವನ್ನು
   ↓
ಪ್ರೀತಿಸುತ್ತೇನೆ
   ↓
<END>
```

This is called **autoregressive generation**.

---

# 11. Why does the Decoder generate one token at a time?

The Decoder cannot simply see the complete answer and copy it.

It generates the output step by step.

For example:

### Step 1

```text
<START>
```

Predict:

```text
ನಾನು
```

### Step 2

Now the Decoder has:

```text
<START> ನಾನು
```

Predict:

```text
ಭಾರತವನ್ನು
```

### Step 3

Now:

```text
<START> ನಾನು ಭಾರತವನ್ನು
```

Predict:

```text
ಪ್ರೀತಿಸುತ್ತೇನೆ
```

### Step 4

```text
<START> ನಾನು ಭಾರತವನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ
```

Predict:

```text
<END>
```

Therefore:

```text
Decoder = Generate → Generate → Generate → Stop
```

---

# 12. Decoder has Masked Self-Attention

There is an important difference between Encoder Self-Attention and Decoder Self-Attention.

The Encoder can see the complete input:

```text
I love India
```

But while generating the output, the Decoder should not be allowed to see future tokens.

Suppose the correct output is:

```text
ನಾನು ಭಾರತವನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ
```

When generating `ಭಾರತವನ್ನು`, the Decoder should only know:

```text
ನಾನು
```

It should NOT know:

```text
ಪ್ರೀತಿಸುತ್ತೇನೆ
```

because that token is in the future.

This is why the Decoder uses **Masked Self-Attention**.

---

# 13. How Masking Works

Suppose the output is:

```text
ನಾನು भारतವನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ
```

Conceptually, the attention looks like this:

```text
Current Token        Can Attend To

ನಾನು                 나는
ಭಾರತವನ್ನು             나는 + भारतವನ್ನು
ಪ್ರೀತಿಸುತ್ತೇನೆ         나는 + भारतವನ್ನು + प्रीतಿಸುತ್ತೇನೆ
```

Future tokens are hidden.

```text
        나는   ಭಾರತವನ್ನು   ಪ್ರೀತಿಸುತ್ತೇನೆ

ನಾನು       ✓       ✗           ✗

ಭಾರತವನ್ನು  ✓       ✓           ✗

ಪ್ರೀತಿಸುತ್ತೇನೆ
            ✓       ✓           ✓
```

This is called **causal masking** or **look-ahead masking**.

The purpose is simple:

> The Decoder should only use information that is already available while generating the output.

---

# 14. Encoder-Decoder Attention

The Decoder also needs information from the original input.

This is where **Encoder-Decoder Attention**, also called **Cross-Attention**, is used.

Suppose the Decoder has generated:

```text
ನಾನು
```

Now it needs to decide what should come next.

It can look at the Encoder's representation of:

```text
"I love India"
```

through Cross-Attention.

Conceptually:

```text
                    ENCODER
               "I love India"
                     |
                     |
                  Key + Value
                     |
                     v
              +-------------+
              |    Cross    |
              |  Attention  |
              +-------------+
                     ^
                     |
                   Query
                     |
                  DECODER
                  "ನಾನು"
```

The Decoder is essentially asking:

> "Which information from the input sentence is important for generating my next token?"

---

# 15. Q, K and V in Cross-Attention

This is an important concept.

In Decoder Cross-Attention:

```text
Query
  ↓
comes from Decoder

Key
Value
  ↓
come from Encoder
```

So:

```text
              ENCODER
                 |
          +------+------+
          |             |
         Key          Value
          |             |
          +------+------+
                 |
                 v
          Cross-Attention
                 ^
                 |
               Query
                 |
              DECODER
```

A simple way to remember:

> **Decoder asks the Query, Encoder provides the Key and Value information.**

---

# 16. Complete Encoder Architecture

A simplified Encoder layer looks like this:

```text
Input Embeddings
       +
Positional Encoding
       |
       v
+----------------------+
| Multi-Head           |
| Self-Attention       |
+----------------------+
       |
       v
Add & Norm
       |
       v
+----------------------+
| Feed Forward         |
| Network              |
+----------------------+
       |
       v
Add & Norm
       |
       v
Encoder Output
```

The original Transformer contains multiple Encoder layers stacked together.

---

# 17. Complete Decoder Architecture

A simplified Decoder layer looks like this:

```text
Output Embeddings
       +
Positional Encoding
       |
       v
+----------------------+
| Masked Multi-Head    |
| Self-Attention       |
+----------------------+
       |
       v
Add & Norm
       |
       v
+----------------------+
| Encoder-Decoder      |
| Attention            |
| (Cross-Attention)    |
+----------------------+
       |
       v
Add & Norm
       |
       v
+----------------------+
| Feed Forward         |
| Network              |
+----------------------+
       |
       v
Add & Norm
       |
       v
Linear Layer
       |
       v
Softmax
       |
       v
Next Token
```

Again, the original Transformer uses multiple Decoder layers.

---

# 18. What happens at the final stage?

After the Decoder processes the information, the output goes through:

```text
Decoder Output
      |
      v
Linear Layer
      |
      v
Vocabulary Scores
      |
      v
Softmax
      |
      v
Probability for each token
```

For example:

```text
나는          → 0.05
भारतವನ್ನು     → 0.10
ಪ್ರೀತಿಸುತ್ತೇನೆ → 0.70
India         → 0.02
love          → 0.01
...
```

The model selects the next token based on these probabilities.

---

# 19. Complete Transformer Flow

Now we can connect everything together.

```text
                    INPUT
                "I love India"
                      |
                      v
               Tokenization
                      |
                      v
              Token Embeddings
                      |
                      v
            Positional Encoding
                      |
                      v
              +-------------+
              |   ENCODER   |
              |             |
              | Self        |
              | Attention   |
              |     ↓       |
              | Add & Norm  |
              |     ↓       |
              | Feed Forward|
              |     ↓       |
              | Add & Norm  |
              +------+------+
                     |
                     |
              Encoder Output
                     |
                     |
                     v
              +-------------+
              |   DECODER   |
              |             |
Output Tokens →| Masked      |
              | Self-Attn   |
              |     ↓       |
              | Cross-Attn  | ← Encoder Output
              |     ↓       |
              | Feed Forward|
              |     ↓       |
              | Linear      |
              |     ↓       |
              | Softmax     |
              +------+------+
                     |
                     v
                  OUTPUT

        "ನಾನು ಭಾರತವನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ"
```

---

# 20. Encoder vs Decoder

| Encoder                             | Decoder                           |
| ----------------------------------- | --------------------------------- |
| Processes input                     | Generates output                  |
| Understands input context           | Generates output context          |
| Uses Self-Attention                 | Uses Masked Self-Attention        |
| Can see all input tokens            | Cannot see future output tokens   |
| Produces contextual representations | Produces next-token probabilities |
| Provides information to Decoder     | Uses Encoder information          |

The easiest way to remember:

```text
ENCODER
   ↓
UNDERSTAND

DECODER
   ↓
GENERATE
```

---

# 21. Self-Attention vs Cross-Attention

This distinction is very important.

### Self-Attention

Attention happens within the same sequence.

```text
Input
  ↓
Self-Attention
  ↓
Input tokens attend to input tokens
```

Example:

```text
I ↔ love ↔ India
```

### Cross-Attention

Attention happens between two different sequences/components.

```text
Decoder
   |
   | Query
   v
Cross-Attention
   ^
   | Key + Value
   |
Encoder
```

Therefore:

```text
Self-Attention
→ "Look at my own sequence"

Cross-Attention
→ "Look at information from another sequence"
```

---

# 23. Training vs Inference

### During Training

```text
Input
  ↓
Encoder
  ↓
Encoder Representation
  ↓
Decoder + Target Information
  ↓
Prediction
  ↓
Compare with actual answer
  ↓
Calculate Loss
  ↓
Update Model
```

### During Inference

```text
Input
  ↓
Encoder
  ↓
Encoder Representation
  ↓
Decoder
  ↓
Generate Token
  ↓
Feed Generated Token Back
  ↓
Generate Next Token
  ↓
Repeat
  ↓
<END>
```

---

# 24. Original Transformer vs Modern LLMs

The original Transformer architecture introduced in the 2017 paper contains:

```text
Encoder + Decoder
```

But modern Transformer models can use different architectures.

### Encoder-only

Example:

```text
BERT
```

Main purpose:

```text
Understanding / Representation Learning
```

Architecture:

```text
Input
  ↓
Encoder
  ↓
Representation
```

### Decoder-only

Examples:

```text
GPT-style models
```

Main purpose:

```text
Text Generation
```

Architecture:

```text
Previous Tokens
      ↓
Decoder
      ↓
Next Token
```

### Encoder-Decoder

Examples include:

```text
T5
```

Main purpose:

```text
Input → Output transformation
```

Architecture:

```text
Input
  ↓
Encoder
  ↓
Representation
  ↓
Decoder
  ↓
Output
```

---

# 25. One-Line Revision Notes

Remember these points for interviews and revision:

```text
Encoder
→ Understands/processes the input.

Decoder
→ Generates the output.

Tokenization
→ Converts text into tokens.

Embedding
→ Converts tokens into numerical vectors.

Positional Encoding
→ Provides information about token positions.

Self-Attention
→ Tokens attend to other tokens in the same sequence.

Masked Self-Attention
→ Prevents the Decoder from looking at future tokens.

Cross-Attention
→ Decoder attends to Encoder representations.

Q
→ Query: What information am I looking for?

K
→ Key: What information is available?

V
→ Value: What information should be retrieved?

Linear + Softmax
→ Converts Decoder output into token probabilities.

Autoregressive Generation
→ Generate one token, use it to generate the next token.
```

---

# 26. The Most Important Mental Model

If you remember only one diagram, remember this:

```text
                 TRANSFORMER
                     |
          +----------+----------+
          |                     |
       ENCODER               DECODER
          |                     |
     "Understand"           "Generate"
          |                     |
          |                Masked Self-Attn
          |                     |
          |                Cross-Attention
          |                     ^
          |                     |
          +---------------------+
             Encoder Context
                     |
                     v
              Next Token
```

### Final takeaway

> **The Encoder reads and builds an understanding of the input. The Decoder uses that understanding and the tokens generated so far to produce the output one token at a time.**

For the original Transformer:

```text
INPUT
  ↓
ENCODER
  ↓
CONTEXTUAL REPRESENTATION
  ↓
DECODER
  ↓
NEXT TOKEN
  ↓
NEXT TOKEN
  ↓
NEXT TOKEN
  ↓
OUTPUT
```

That is the core idea behind **Transformer Encoder-Decoder architecture**.
