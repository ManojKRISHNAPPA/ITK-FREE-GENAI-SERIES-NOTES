# Module 02 — Basic Prompting Techniques

> "Zero-shot is asking a stranger for directions. Few-shot is showing them a map first."

---

## 2.1 Zero-Shot Prompting

**Zero-shot** = giving the model a task with NO examples. Just the instruction.

This works well when:
- The task is straightforward.
- The model has seen similar tasks in training.

### Example: Sentiment Analysis (Zero-Shot)
```
Classify the sentiment of the following review as Positive, Negative, or Neutral.

Review: "The food was amazing but the service was painfully slow."

Answer:
```

**Expected Output:**
```
Mixed (Positive food, Negative service)
```

---

### Example: Translation (Zero-Shot)
```
Translate the following English sentence to French:

"I would like to book a table for two people at 7pm."
```

**Output:**
```
"Je voudrais réserver une table pour deux personnes à 19h."
```

---

### When Zero-Shot Fails

Zero-shot struggles with:
- Niche formats the model hasn't seen
- Complex multi-step tasks
- Tasks requiring a specific style or tone you haven't described

**Fix:** Add examples → use Few-Shot.

---

## 2.2 One-Shot Prompting

**One-shot** = provide exactly ONE example to demonstrate the desired behavior.

### Example: Custom Data Extraction
```
Extract the name and city from the text below.

Example:
Text: "Hi, I'm Priya and I live in Bangalore."
Output: Name: Priya | City: Bangalore

Now do this:
Text: "My name is Carlos and I'm based in Mexico City."
Output:
```

**Expected Output:**
```
Name: Carlos | City: Mexico City
```

One example teaches the model your **exact format**.

---

## 2.3 Few-Shot Prompting

**Few-shot** = provide 2–5 examples before the actual task. This is the most powerful basic technique.

### Why it Works

The model learns the **pattern** from your examples and replicates it. You're not explaining — you're demonstrating.

> Rule of thumb: 3 examples is usually the sweet spot.

---

### Example: Custom Classification

```
Classify customer support tickets into: Billing, Technical, General

Ticket: "I was charged twice this month."
Category: Billing

Ticket: "My app keeps crashing when I open settings."
Category: Technical

Ticket: "What are your business hours?"
Category: General

Ticket: "I can't log in and it says my account is suspended."
Category:
```

**Expected Output:**
```
Technical
```

---

### Example: Data Transformation (Few-Shot)

```
Convert the informal date to ISO 8601 format (YYYY-MM-DD).

"3rd of January 2024" → 2024-01-03
"15th August, 1947" → 1947-08-15
"December 25th, 2023" → 2023-12-25

"7th of July 2025" →
```

**Expected Output:**
```
2025-07-07
```

---

### Example: Tone Transformation

```
Rewrite the text to sound formal and professional.

Informal: "Hey! Wanna grab a call sometime this week to chat about the project?"
Formal: "I would like to schedule a call at your earliest convenience to discuss the project."

Informal: "This is super confusing and I have no idea what's going on."
Formal: "I am experiencing some difficulty understanding the current situation and would appreciate clarification."

Informal: "The boss totally flipped out at the meeting lol."
Formal:
```

**Expected Output:**
```
The manager expressed significant concern during the meeting.
```

---

## 2.4 Comparing the Three Approaches

| Technique | Examples Given | Best For | Risk |
|-----------|---------------|----------|------|
| Zero-shot | 0 | Simple, common tasks | Vague output |
| One-shot | 1 | Format-specific tasks | Overfitting to 1 example |
| Few-shot | 2–5 | Complex/custom tasks | Long prompt, token cost |

---

## 2.5 Designing Good Examples

Bad examples mislead the model. Good examples teach it exactly what you want.

### Rules for Good Examples

1. **Be consistent** — same format in every example.
2. **Cover edge cases** — include tricky examples, not just easy ones.
3. **Match the real input** — your examples should look like your real data.
4. **Don't contradict** — all examples should follow the same logic.

### Bad Example Set
```
Text: "Happy" → Positive
Text: "Sad. But also kind of okay." → Negative  ← inconsistent logic
Text: "GREAT!!!" → positive  ← inconsistent casing
```

### Good Example Set
```
Text: "Happy" → Positive
Text: "Really disappointed with the product." → Negative
Text: "It arrived on time. Nothing special." → Neutral
```

---

## 2.6 Practice Exercises

### Exercise 1
Create a 3-shot prompt that extracts structured data from job descriptions.
Input: raw job posting text.
Output: `Role | Company | Location | Salary`

### Exercise 2
Create a zero-shot prompt to detect if a text contains a phone number.
Output should be: `Yes` or `No`.

### Exercise 3
Create a one-shot prompt that converts bullet points into a numbered executive summary.

---

## 2.7 Summary

- **Zero-shot**: no examples, just instructions.
- **One-shot**: one example to set format.
- **Few-shot**: 2–5 examples to teach complex patterns.
- Few-shot is powerful but costs more tokens.
- Your examples ARE the training data — make them good.

---

*Next: [03-chain-of-thought.md](./03-chain-of-thought.md) — Making AI reason step by step*
