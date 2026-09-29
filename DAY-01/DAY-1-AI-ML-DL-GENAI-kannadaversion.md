# ITkannadigaru - AI, Machine Learning, Deep Learning, and Generative AI

> **Learning path:** AI -> Machine Learnineep Learning -> Generative AI -> LLMs -> RAG -> AI Agentsg -> D

---

## 1. What Is Artificial Intelligence?

**Artificial Intelligence (AI)** is the technology that enables machines to perform tasks that normally require human intelligence.

### Examples

- Google Maps - route prediction
- Netflix - movie recommendations
- Google Photos - face recognition
- Banking systems - fraud detection
- ChatGPT - language understanding and generation
- Self-driving cars - object detection and decision-making

### Rule-Based AI

In rule-based AI, developers manually define the rules.

```text
IF transaction_amount > INR 100,000
AND country != user's_country
AND transaction_time = 3 AM
THEN mark the transaction as suspicious
```

This approach works for simple situations. However, writing rules for every possible real-world situation is difficult.

---

## 2. What Is Machine Learning?

**Machine Learning (ML)** is an approach in which machines learn patterns from data instead of being explicitly programmed with every rule.

### Traditional Programming vs Machine Learning

| Traditional Programming | Machine Learning |
|---|---|
| Rules + Data -> Program -> Output | Data + Expected Output -> Algorithm -> Model |
| Developers write the rules | The model learns patterns from data |
| Suitable for fixed logic | Suitable for complex patterns |

After training:

```text
New Data -> Trained Model -> Prediction
```

### Algorithm vs Model

- **Algorithm:** A mathematical procedure used to learn patterns from data.
- **Model:** The trained result containing the relationships and parameters learned by the algorithm.

---

## 3. Relationship Between AI, ML, Deep Learning, and GenAI

```text
Artificial Intelligence
|-- Rule-Based AI
`-- Machine Learning
    |-- Classical Machine Learning
    `-- Deep Learning
        |-- CNN
        |-- RNN/LSTM
        `-- Transformers
```

Most modern **Generative AI** systems use deep learning architectures, especially Transformers.

### Remember

- AI is the broad umbrella.
- ML is one approach used to build AI systems.
- Deep Learning is a subset of ML.
- Generative AI creates new content from learned patterns.

---

## 4. What Is Data?

Data is the foundation of every AI and ML system.

```text
Data -> Preparation -> Training -> Model -> Prediction
```

### Structured Data

Structured data is organized into rows and columns.

| ID | Name | Age | Salary |
|---:|---|---:|---:|
| 1 | Raj | 25 | INR 50,000 |
| 2 | Ravi | 30 | INR 70,000 |

Common sources include MySQL, PostgreSQL, CSV files, Excel files, and data warehouses.

### Unstructured Data

Unstructured data does not follow a fixed table format.

- PDF files and documents
- Images
- Audio
- Video
- Emails
- Free-form text

Models usually convert unstructured data into numerical representations.

```text
Text -> Tokenizer -> Tokens -> Embeddings -> Model
```

---

## 5. How Does ML Training Work?

Consider a house-price prediction dataset:

| Area | Bedrooms | Location | Price |
|---:|---:|---|---:|
| 1,000 sq ft | 2 | Bengaluru | INR 50 lakh |
| 1,500 sq ft | 3 | Bengaluru | INR 80 lakh |
| 2,000 sq ft | 3 | Bengaluru | INR 1 crore |

During training, the model learns relationships between the inputs and the output.

```text
Historical House Data
        |
        v
   ML Algorithm
        |
        v
      Training
        |
        v
   Trained Model
        |
        v
New House Details -> Predicted Price
```

### Training Steps

1. **Collect data** - Gather data relevant to the problem.
2. **Clean data** - Handle null values, duplicates, invalid values, outliers, and inconsistent formats.
3. **Create or select features** - Prepare useful inputs for the model.
4. **Split the data** - Create training, validation, and test datasets.
5. **Train the model** - Use an algorithm to learn patterns.
6. **Evaluate the model** - Measure performance on unseen data.
7. **Deploy and monitor** - Use the model in production and track its behavior.

---

## 6. Features and Labels

**Features** are the input variables given to a model.  
The **label** or **target** is the output that the model must predict.

| Type | Example |
|---|---|
| Feature | Area |
| Feature | Number of bedrooms |
| Feature | Location |
| Target | House price |

```text
Area ---------\
Bedrooms ------> Model -> Price
Location -----/
```

---

## 7. Training, Validation, and Test Data

We should not use all available data for training.

A common split is:

| Dataset | Example Split | Purpose |
|---|---:|---|
| Training data | 80% | Used by the model to learn patterns |
| Validation data | 10% | Used to tune hyperparameters and model choices |
| Test data | 10% | Used for final evaluation on unseen data |

The exact percentages can change depending on the problem and dataset size.

---

## 8. Main Types of Machine Learning

### Supervised Learning

The training data contains inputs and their correct outputs. It is similar to learning with a teacher.

```text
Input + Correct Answer -> Training -> Prediction
```

Example: Email -> Spam or Not Spam

### Unsupervised Learning

The data has no labels. The model searches for groups, structures, or patterns.

Example: Customers -> Groups of similar customers

### Reinforcement Learning

An agent learns by taking actions in an environment and receiving rewards or penalties.

```text
Agent -> Action -> Environment -> Reward/Penalty -> Learning
```

Common uses include robotics, game playing, control systems, and optimization.

### Other Learning Types

- **Semi-Supervised Learning:** Uses a small amount of labeled data and a larger amount of unlabeled data.
- **Self-Supervised Learning:** Creates a training signal from the data itself. It is widely used in LLM pretraining.

---

## 9. Regression

**Regression** predicts a continuous numerical value.

### Examples

- House -> INR 90 lakh
- Employee -> INR 15 lakh annual salary
- Temperature -> 32.5 degrees Celsius
- Monthly sales -> INR 520,000

### Simple Linear Regression

The basic idea is to find a best-fit line that represents the overall pattern in the data.

```text
Price
  |             *
  |         *
  |      *
  |   *
  | *
  +---------------- Area
```

Formula:

```text
y_hat = b0 + b1*x
```

- `y_hat` - predicted value
- `x` - input feature
- `b0` - intercept
- `b1` - slope

---

## 10. Classification

**Classification** predicts a category or class.

### Examples

- Email -> Spam or Not Spam
- Transaction -> Fraud or Genuine
- Customer -> Churn or No Churn
- Image -> Cat or Dog

### Types of Classification

- **Binary Classification:** Predicts one of two classes, such as Yes or No.
- **Multiclass Classification:** Predicts one of several classes, such as Cat, Dog, Horse, or Bird.

### Common Algorithms

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

Although its name contains the word "Regression," Logistic Regression is commonly used for classification.

---

## 11. Clustering and Unsupervised Learning

**Clustering** groups similar data points without using predefined labels.

```text
Customer Data
     |
     v
Clustering Algorithm
     |
     v
Premium | Discount-Focused | Occasional
```

A popular clustering algorithm is **K-Means**.

Common uses include customer segmentation, anomaly discovery, and market analysis.

---

## 12. Deep Learning

**Deep Learning** is a branch of Machine Learning that uses neural networks with multiple layers.

Classical ML may depend heavily on manually designed features. Deep Learning can learn useful representations directly from large datasets.

```text
Input Layer -> Hidden Layers -> Output Layer
```

### Important Neural Network Terms

- **Weight:** A learned value representing the importance of an input.
- **Bias:** A learned value that adjusts a neuron's output.
- **Activation Function:** Helps the network learn complex, non-linear patterns.
- **Loss Function:** Measures how incorrect a prediction is.
- **Gradient Descent:** An optimization method used to reduce loss.
- **Backpropagation:** Sends error information backward through the network to update weights.
- **Epoch:** One complete pass through the training dataset.

---

## 13. How Does a Neural Network Learn?

```text
Input
  |
  v
Prediction
  |
  v
Compare with Actual Value
  |
  v
Calculate Loss
  |
  v
Backpropagation
  |
  v
Update Weights
  |
  v
Repeat
```

Example:

```text
Actual Price     = INR 100 lakh
Model Prediction = INR 70 lakh
```

The system calculates the error and adjusts its weights to improve future predictions.

---

## 14. Overfitting and Underfitting

### Overfitting

Overfitting occurs when a model performs very well on training data but poorly on unseen data.

```text
Training Data -> Excellent
New Data      -> Poor
```

It is similar to a student memorizing textbook answers but failing to answer new questions.

### Underfitting

Underfitting occurs when a model fails to learn even the basic patterns in the training data.

```text
Training Data -> Poor
New Data      -> Poor
```

A good model should perform well on training data and **generalize** to unseen data.

---

## 15. CNN, RNN/LSTM, and Transformers

| Architecture | Main Use |
|---|---|
| CNN | Images and computer vision |
| RNN/LSTM | Sequential data, time series, text, and speech |
| Transformer | Modern NLP, LLMs, and multimodal AI |

### CNN Example

```text
X-Ray -> CNN -> Edges -> Shapes -> Patterns -> Disease Prediction
```

### Transformers and Attention

Consider this sentence:

> "I deposited money in the bank."

The meaning of `bank` becomes clear from the surrounding words. The **attention** mechanism helps a model identify relevant relationships between tokens.

```text
Input -> Tokenization -> Embeddings -> Transformer -> Contextual Representation
```

---

## 16. What Is Generative AI?

Traditional ML usually predicts a value or category. Generative AI creates new content based on learned patterns.

### Examples

- Text -> Text
- Text -> Image
- Text -> Code
- Text -> Audio
- Text -> Video
- Text + Image + Audio -> Multimodal response

Generative AI is not limited to LLMs. For example, many image-generation systems use diffusion models.

---

## 17. What Is a Large Language Model?

**LLM** stands for **Large Language Model**.

An LLM is trained on a very large amount of text and code. At a simplified level, one of its main training tasks is **next-token prediction**.

```text
"The capital of India is" -> Delhi
```

### LLM Processing Flow

```text
Text
  |
  v
Tokenization
  |
  v
Tokens
  |
  v
Embeddings
  |
  v
Transformer
  |
  v
Next-Token Probabilities
  |
  v
Generated Response
```

- **Token:** A unit of text processed by a model. It may be a word, part of a word, or punctuation.
- **Embedding:** A numerical vector representing a token's meaning and relationships.
- **Context Window:** The maximum number of tokens a model can process together.

An LLM can produce incorrect information. Important answers should always be verified.

---

## 18. Pretraining and Fine-Tuning

### Pretraining

Pretraining creates a base or foundation model by training it on a massive general-purpose dataset.

```text
Large Text and Code Dataset -> Training -> Base Model
```

### Fine-Tuning

Fine-tuning trains a base model further using data for a specific task or domain.

```text
Base Model + Domain Data -> Fine-Tuned Model
```

Example: General model + medical data -> Medical-focused model

---

## 19. Retrieval-Augmented Generation

**RAG** stands for **Retrieval-Augmented Generation**.

An LLM may not know private, company-specific, or recently updated information. RAG retrieves relevant documents and provides them to the LLM as context.

```text
User Question
      |
      v
Question Embedding
      |
      v
Vector Search
      |
      v
Relevant Documents
      |
      v
Question + Retrieved Context
      |
      v
LLM
      |
      v
Answer
```

### Example

Question: "What is our company's leave policy?"

The system searches company documents in a vector database, retrieves the relevant policy, and gives that context to the LLM.

### Important Point

RAG is not a new category of Machine Learning. It is an **application architecture** built around an LLM.

---

## 20. What Is an AI Agent?

An LLM mainly generates responses. An **AI Agent** combines a model with tools or APIs so that it can perform actions.

```text
User Request
    |
    v
LLM Understands Intent
    |
    v
Select Tool
    |
    v
Call API
    |
    v
Observe Result
    |
    v
Continue or Return Final Answer
```

Example request:

> "Find my latest order and cancel it."

Possible agent flow:

```text
Find Order API -> Get Latest Order -> Cancellation API -> Confirm Result
```

### LLM vs RAG vs AI Agent

| System | Main Purpose |
|---|---|
| LLM | Generates content from learned knowledge |
| RAG | Retrieves external documents to generate a grounded answer |
| AI Agent | Uses tools and APIs in a reasoning loop to complete a task |

---

## 21. End-to-End AI Engineer View

### Traditional ML System

```text
Data
  |
  v
Data Preparation
  |
  v
Feature Engineering
  |
  v
Algorithm and Training
  |
  v
Model Evaluation
  |
  v
Deployment
  |
  v
Prediction
  |
  v
Monitoring
```

### Generative AI Application

```text
User Input
   |
   v
Prompt / Retrieval / Tools
   |
   v
Foundation Model
   |
   v
Application Logic
   |
   v
API / Agent
   |
   v
Production
   |
   v
Evaluation and Monitoring
```

An AI Engineer needs model knowledge as well as skills in APIs, Docker, Kubernetes, CI/CD, security, evaluation, observability, and production monitoring.

---

## 22. E-Commerce Examples

| Problem | Suitable Approach |
|---|---|
| Predict sales amount | Regression |
| Identify fraud or genuine transactions | Classification |
| Group similar customers | Clustering |
| Identify product-image categories | CNN or vision model |
| Answer a customer question | LLM |
| Answer using company documents | RAG |
| Find and cancel an order | AI Agent with APIs |

---

## 23. Quick Revision Questions and Answers

1. **What is AI?**  
   AI enables machines to perform tasks that normally require human intelligence.

2. **What is ML?**  
   ML is an AI approach in which machines learn patterns from data instead of following only manually written rules.

3. **What is the difference between an algorithm and a model?**  
   An algorithm is the learning procedure; a model is the trained output of that procedure.

4. **What is a feature?**  
   A feature is an input variable given to a model.

5. **What is a label or target?**  
   It is the output that the model must predict.

6. **When is regression used?**  
   Regression is used to predict a continuous numerical value.

7. **When is classification used?**  
   Classification is used to predict a category or class.

8. **What is clustering?**  
   Clustering groups similar data points without predefined labels.

9. **What is an epoch?**  
   An epoch is one complete pass through the training dataset.

10. **What is overfitting?**  
    It occurs when a model performs well on training data but poorly on unseen data.

11. **What is the key idea behind Transformers?**  
    Transformers use attention to learn contextual relationships between tokens.

12. **How does an LLM generate text?**  
    It predicts tokens sequentially based on the available context.

13. **What is fine-tuning?**  
    Fine-tuning trains a base model further for a specific task or domain.

14. **Why is RAG used?**  
    RAG retrieves external, private, or current information to produce a more grounded answer.

15. **What is the difference between an LLM and an AI Agent?**  
    An LLM generates responses, while an agent can use tools and APIs to perform actions.

---

## 24. One-Line Summary

> **Machine Learning learns patterns from data; Deep Learning learns complex representations through neural networks; Generative AI uses learned representations to create new content; RAG adds external knowledge; and AI Agents use tools to complete tasks.**

---

## 25. Recommended Learning Order

1. AI vs ML vs Deep Learning vs Generative AI
2. Data, features, labels, and dataset splitting
3. Regression, classification, and clustering
4. Neural networks, loss, gradient descent, and backpropagation
5. CNNs, RNN/LSTMs, and Transformers
6. Tokens, embeddings, and LLMs
7. Prompting, fine-tuning, and evaluation
8. RAG and vector databases
9. AI Agents, tools, and APIs
10. Docker, Kubernetes, CI/CD, monitoring, and production AI

---

**Channel:** ITkannadigaru  
**Purpose:** To make AI concepts simple and accessible while preserving the English technical terminology needed for interviews and real-world projects.
