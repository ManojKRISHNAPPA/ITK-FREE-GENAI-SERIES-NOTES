# Module 01 — Foundations of Prompt Engineering

> "Before you can drive a car, you must understand it has a steering wheel, not a magic wand."

---

## 1.1 How Language Models Think

Large Language Models (LLMs) are **next-token predictors**. They don't "think" — they predict the most statistically likely continuation of text based on billions of training examples.

This means:
- They are pattern matchers, not reasoners (by default).
- The prompt is the **entire context** they have.
- They have no memory between conversations.
- They don't know what you *meant* — only what you *wrote*.

### Mental Model

```
Your Prompt → [LLM] → Predicted Continuation
```

The model asks itself: *"Given this text, what comes next?"*

Your job: **write a prompt that makes the right answer the most likely continuation.**

---

## 1.2 Anatomy of a Prompt

Every prompt has up to four parts:

```
┌─────────────────────────────────────────┐
│  CONTEXT      (background info)         │
│  INSTRUCTION  (what you want done)      │
│  INPUT        (the data to work on)     │
│  OUTPUT FORMAT (how you want the result)│
└─────────────────────────────────────────┘
```

You don't always need all four — but the more you include, the more control you have.

---

## 1.3 Your First Prompt — Weak vs Strong

### Weak Prompt
```
Tell me about Python.
```

**Problem:** "About" is vague. Python the language? Python the snake? A 2-sentence overview or a 10,000-word essay?

---

### Strong Prompt
```
You are a programming teacher explaining Python to a complete beginner.

In 3 bullet points, explain:
1. What Python is
2. Why it's popular
3. One real-world thing you can build with it

Keep each point under 2 sentences.
```

**Why it's better:**
- Role set ("programming teacher")
- Audience defined ("complete beginner")
- Structure specified ("3 bullet points")
- Scope limited ("under 2 sentences each")

---

## 1.4 The 5 Dimensions of a Good Prompt

| Dimension | Question to Ask Yourself |
|-----------|--------------------------|
| **Clarity** | Is there any ambiguous word in my prompt? |
| **Context** | Does the model have enough background? |
| **Specificity** | Am I being precise about what I want? |
| **Format** | Have I told the model how to structure the answer? |
| **Constraints** | Have I set any boundaries (length, tone, scope)? |

---

## 1.5 Exercise: Rewrite These Weak Prompts

Try improving these before looking at the answers.

**Weak #1:** `Explain machine learning`  
**Weak #2:** `Write me an email`  
**Weak #3:** `Give me ideas`  

---

### Improved Versions

**Strong #1:**
```
Explain machine learning to a 15-year-old with no technical background.
Use a real-world analogy (not self-driving cars).
Keep it under 100 words.
```

**Strong #2:**
```
Write a professional follow-up email to a client named Sarah at Acme Corp.
Context: We met at a conference last Tuesday and discussed a potential
partnership for data analytics services.
Tone: Warm but professional.
Length: 3 short paragraphs.
Include a clear call-to-action asking for a 30-minute call this week.
```

**Strong #3:**
```
I'm a solo developer launching a SaaS product for restaurant owners.
Give me 5 creative marketing ideas for social media.
Each idea should be actionable in under 1 hour and cost $0.
Format: numbered list with a one-line explanation for each.
```

---

## 1.6 Key Concepts Glossary

| Term | Definition |
|------|-----------|
| **Token** | A chunk of text (~4 chars). LLMs process tokens, not words. |
| **Context window** | Maximum tokens the model can see at once. |
| **System prompt** | Instructions given to the model before the user speaks. |
| **Temperature** | Controls randomness. 0 = deterministic, 1+ = creative. |
| **Hallucination** | Model confidently states false information. |
| **Grounding** | Giving the model real data so it doesn't hallucinate. |

---

## 1.7 Summary

- LLMs predict tokens — they follow patterns.
- Your prompt is ALL the context the model has.
- A good prompt has: Context + Instruction + Input + Output Format.
- Ambiguity = bad output. Clarity = good output.

---

## Checkpoint Questions

1. Why does a vague prompt produce vague output?
2. What are the 4 parts of a well-structured prompt?
3. What does "temperature" control in an LLM?

---

*Next: [02-basic-techniques.md](./02-basic-techniques.md) — Zero-shot, One-shot, Few-shot*
