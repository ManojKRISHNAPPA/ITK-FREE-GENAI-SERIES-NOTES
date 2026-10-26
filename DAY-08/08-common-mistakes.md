# Module 08 — Common Mistakes & How to Fix Them

> "Every bad output is diagnostic. It tells you exactly what was missing from the prompt."

---

## 8.1 The Mindset Shift

When an LLM gives you a bad response, resist the urge to think "the AI is dumb."

Instead ask: **"What did my prompt assume that the model didn't know?"**

The model isn't wrong. It did exactly what your prompt implied. You just implied the wrong thing.

---

## 8.2 Mistake #1 — Vague Instructions

### The Problem
```
❌ Write a summary.
```

Summary of what? For whom? How long? What format?

### The Fix
```
✅ Summarize the following article in 3 sentences for a busy executive.
   Focus on: the main finding, the business implication, and the recommended action.
```

**Rule:** Every noun in your instruction should be qualified. Every verb should have a clear scope.

---

## 8.3 Mistake #2 — Assuming Context

### The Problem
```
❌ Continue the story from where we left off.
```

The model has no persistent memory. "Where we left off" doesn't exist in a new session.

### The Fix
```
✅ Here is the story so far: [paste full text]

Continue the story from the end of the last paragraph. 
The protagonist has just discovered the letter. Next scene: the confrontation.
```

**Rule:** Never assume the model knows context from a previous session, a document you haven't shared, or a conversation it can't see.

---

## 8.4 Mistake #3 — Asking for Everything at Once

### The Problem
```
❌ Analyze this business, suggest improvements, write a marketing plan, create a budget, 
   and draft 3 months of social media posts.
```

Cramming too many tasks produces shallow results across all of them.

### The Fix
Break it into a **prompt chain**:
```
✅ Step 1: Analyze the strengths and weaknesses of this business. (Done first, reviewed)
   Step 2: Based on your analysis, suggest 3 high-impact improvements. (Uses Step 1)
   Step 3: For improvement #2, write a detailed marketing plan. (Focused)
```

**Rule:** One clear objective per prompt. Chain them sequentially.

---

## 8.5 Mistake #4 — Ignoring Format

### The Problem
```
❌ List all the features of the product.
```

You get a rambling paragraph when you wanted bullet points.

### The Fix
```
✅ List all features of the product.
   Format: bullet points, one feature per line, max 8 words each.
```

**Rule:** Always specify format unless you genuinely don't care.

---

## 8.6 Mistake #5 — Asking for Opinions Without Framing

### The Problem
```
❌ Is React or Vue better?
```

The model gives a diplomatic non-answer: "It depends on your use case..."

### The Fix
```
✅ I'm a solo developer building a portfolio website with minimal interactivity.
   I know HTML/CSS but no JavaScript framework yet.
   
   Given this context, give me your definitive recommendation: React or Vue?
   State your recommendation first, then explain the top 3 reasons.
   Acknowledge the main downside of your recommendation.
```

**Rule:** Give enough context that there IS a right answer. Vague questions get vague answers.

---

## 8.7 Mistake #6 — Prompt Stuffing

### The Problem
```
❌ You are an expert AI assistant who is helpful, harmless, and honest, 
   deeply knowledgeable about all topics, a great writer, creative, 
   thoughtful, precise, detailed, concise when needed but thorough 
   when important, and always considers multiple perspectives...
   
   What is Python?
```

Excessive preamble dilutes the signal. The model doesn't get "more expert" by being told it is.

### The Fix
```
✅ You are a Python instructor for beginners.
   What is Python?
```

**Rule:** Every word in your prompt should carry information. Remove words that don't change what the model would produce.

---

## 8.8 Mistake #7 — Trusting Numbers Without Verification

### The Problem
```
You: "What's the market size for AI in 2024?"
AI: "The global AI market is $142.3 billion in 2024, growing at 37.3% CAGR..."
```

These numbers SOUND precise but may be hallucinated or outdated.

### The Fix
```
✅ What is the approximate market size for AI in 2024?
   If you're uncertain of the exact figure, give a range and indicate your confidence.
   Do NOT cite statistics you cannot verify. 
   Recommend 2-3 authoritative sources I should check for the latest data.
```

**Rule:** Ask for ranges and confidence levels. Ask for sources. Verify any statistic before using it.

---

## 8.9 Mistake #8 — Accepting the First Response

The first response is a starting point, not a final answer.

### The Fix — Iterative Refinement Loop

```
Response 1: [model output]

Follow-up: "The second paragraph is weak. Rewrite it to be more specific."
Follow-up: "Now make the whole thing 30% shorter."
Follow-up: "Change the opening line — it's too generic."
```

**Rule:** Plan for 2–3 refinement rounds. Treat prompting as a conversation, not a request.

---

## 8.10 Mistake #9 — No Persona = No Consistency

### The Problem
When you don't set a role, the model's tone varies by response — sometimes academic, sometimes casual, sometimes corporate.

### The Fix
Set a role in every prompt or system prompt:
```
✅ You are a direct, no-fluff technical writer.
   You write for engineers who are busy and prefer clarity over elegance.
   Never use filler words. Every sentence must add value.
```

**Rule:** Explicitly set the voice if consistency matters.

---

## 8.11 Mistake #10 — Prompt Once, Deploy Forever

### The Problem
A prompt that works today may fail tomorrow when:
- The model is updated
- Your input data changes
- Edge cases appear that you didn't test

### The Fix

**Build a prompt test suite:**
```
Baseline test: [easy, typical input]
Edge case test: [unusual or minimal input]
Adversarial test: [input designed to break the output format]
Regression test: [previous inputs that worked, run again]
```

**Rule:** Treat prompts like code. Version them. Test them. Review them when behavior changes.

---

## 8.12 Quick Diagnosis Table

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Too long, rambling | No length constraint | Add "in X words/bullets" |
| Too short, shallow | No depth instruction | Ask for examples, detail, elaboration |
| Wrong format | Format not specified | Explicit format instruction |
| Off-topic | Task was ambiguous | Narrow the scope |
| Confident but wrong | No uncertainty instruction | Ask for caveats, sources |
| Generic/boring | No persona or style | Add role + tone |
| Inconsistent across runs | High temperature or no persona | Lower temp, add role |
| Misses key info | Context not provided | Add more background |

---

## 8.13 The Prompt Checklist

Before sending any important prompt, ask:

```
□ Have I stated my task clearly?
□ Have I provided all necessary context?
□ Have I specified the format I want?
□ Have I set a role or persona?
□ Have I defined the audience?
□ Have I constrained the length?
□ Have I set the tone?
□ Have I told it what NOT to do?
□ Is there any word in my prompt that's ambiguous?
□ Am I prepared to refine the output?
```

---

## 8.14 Summary

1. Vague instructions → qualify every noun and verb.
2. Missing context → paste it in, don't assume.
3. Too many tasks → one objective per prompt.
4. No format → always specify.
5. Vague questions → give enough context for a real answer.
6. Prompt stuffing → every word must earn its place.
7. Trusting hallucinated numbers → ask for confidence + sources.
8. Accepting first response → iterate 2–3 times.
9. No persona → always set the voice.
10. One-and-done → test and maintain prompts like code.

---

*Next: [09-real-world-applications.md](./09-real-world-applications.md) — Use cases across domains*
