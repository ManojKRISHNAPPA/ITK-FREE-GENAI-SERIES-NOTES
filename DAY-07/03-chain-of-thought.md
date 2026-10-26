# Module 03 — Chain of Thought (CoT) Prompting

> "Don't ask the model for the answer. Ask it to show its work."

---

## 3.1 What is Chain of Thought?

**Chain of Thought (CoT)** prompting encourages the model to **think step-by-step** before giving a final answer. It dramatically improves accuracy on reasoning tasks.

### Why it Works

LLMs generate tokens left to right. If you ask for an answer directly, the model produces the answer token without "reasoning space." If you ask it to reason first, each reasoning step becomes context for the next — making complex logic possible.

---

## 3.2 Standard Prompting vs CoT

### Problem: Math Word Problem

**Without CoT:**
```
A store has 48 apples. They sell 1/3 in the morning and 1/4 of what's left
in the afternoon. How many apples remain?

Answer:
```

**Model Output (often wrong):** `28` or `24`

---

**With CoT:**
```
A store has 48 apples. They sell 1/3 in the morning and 1/4 of what's left
in the afternoon. How many apples remain?

Let's think step by step:
```

**Model Output:**
```
Step 1: Start with 48 apples.
Step 2: Sell 1/3 in the morning → 48 × (1/3) = 16 sold → 48 - 16 = 32 remain.
Step 3: Sell 1/4 of remaining in afternoon → 32 × (1/4) = 8 sold → 32 - 8 = 24 remain.

Answer: 24 apples remain.
```

The magic phrase: **"Let's think step by step."**

---

## 3.3 Zero-Shot CoT

Adding **"Let's think step by step"** to any prompt activates chain-of-thought reasoning without providing examples.

### Example: Logic Puzzle
```
There are 5 houses in a row. The Englishman lives in the red house.
The Spaniard owns a dog. Coffee is drunk in the green house.
The Ukrainian drinks tea. The green house is immediately to the right of the white house.

Who drinks coffee?

Let's think step by step:
```

**Model will work through each clue systematically** rather than guessing.

---

### Example: Code Debugging
```
This Python function is supposed to return the second largest number in a list,
but it has a bug:

def second_largest(nums):
    nums.sort()
    return nums[-2]

What's the bug and how do I fix it?

Let's think step by step:
```

**Model Output:**
```
Step 1: The function sorts the list in ascending order — correct.
Step 2: nums[-2] gets the second-to-last element — this works for a list
        with unique values.
Step 3: The bug: if there are duplicate maximum values like [5, 5, 3],
        nums[-2] returns 5 again, not 3.

Fix: Remove duplicates first, or use:
def second_largest(nums):
    unique = sorted(set(nums), reverse=True)
    return unique[1] if len(unique) >= 2 else None
```

---

## 3.4 Few-Shot CoT

Combine few-shot examples WITH step-by-step reasoning to teach the model your reasoning format.

### Example: Financial Analysis
```
Q: A product costs $80 to make and sells for $120. What is the profit margin?

A: Let me work through this:
   - Profit = Selling Price - Cost = $120 - $80 = $40
   - Profit Margin = (Profit / Selling Price) × 100 = ($40 / $120) × 100 = 33.3%
   Answer: The profit margin is 33.3%

---

Q: A service costs $200 to deliver and is sold for $350. What is the profit margin?

A:
```

**Model follows the exact reasoning format from the example.**

---

### Example: Decision Analysis
```
Q: Should a startup spend $10,000 on a conference booth?
Context: 500 attendees expected, average deal size $5,000, typical conversion 2%

A: Let me analyze this:
   - Expected leads from booth: 500 attendees × 5% engagement = 25 leads
   - Expected deals: 25 leads × 2% conversion = 0.5 deals
   - Expected revenue: 0.5 × $5,000 = $2,500
   - ROI: ($2,500 - $10,000) / $10,000 = -75%
   Answer: No — the expected ROI is negative. Not recommended unless brand
   awareness is the primary goal.

---

Q: Should a startup spend $3,000 on Google Ads?
Context: 1000 clicks expected, $50 average order value, 3% conversion rate

A:
```

---

## 3.5 Self-Consistency (Advanced CoT)

Generate the **same problem multiple times** with CoT, then take the **majority vote** answer.

### Why It Works
Different reasoning paths can reach the same answer. If 4 out of 5 paths agree, you have higher confidence.

### Prompt Template
```
Solve this problem 3 different ways and then give your final answer based
on the most common result.

Problem: [your problem here]

Method 1:
Method 2:
Method 3:

Final Answer (based on majority):
```

---

## 3.6 When to Use CoT

| Task Type | Use CoT? | Why |
|-----------|----------|-----|
| Math problems | Yes | Multi-step calculation |
| Logic puzzles | Yes | Sequential deduction |
| Code debugging | Yes | Systematic elimination |
| Simple lookup | No | Adds unnecessary length |
| Creative writing | No | Breaks creative flow |
| Factual Q&A | Sometimes | Only if multi-step |

---

## 3.7 CoT Trigger Phrases

These phrases activate step-by-step reasoning:

```
"Let's think step by step."
"Think through this carefully."
"Walk me through your reasoning."
"Before answering, reason through each step."
"Break this down into steps."
"Show your work."
"Think out loud."
```

---

## 3.8 Common CoT Mistakes

### Mistake 1: Using CoT on Simple Tasks
```
❌ What is the capital of France? Let's think step by step.
```
This wastes tokens. Use CoT only when reasoning matters.

### Mistake 2: Not Anchoring the Final Answer
```
❌ (CoT reasoning goes on for 10 steps, no clear final answer)
```

**Fix:** Always end with a clear label:
```
✅ Therefore, the final answer is: [X]
```

### Mistake 3: Accepting Wrong CoT Reasoning
The model can reason confidently AND be wrong. Always sanity-check math.

---

## 3.9 Practice Exercises

### Exercise 1: Enable CoT
Take this prompt and add CoT triggering:
```
A train leaves NYC at 9am going 60mph. Another leaves Boston (215 miles away)
at 10am going 80mph. When do they meet?
```

### Exercise 2: Few-Shot CoT
Create a 2-shot CoT prompt for evaluating whether a business idea is viable.
Include reasoning steps like: market size, competition, differentiation, capital.

### Exercise 3: Debug with CoT
```
def find_average(numbers):
    return sum(numbers) / len(numbers)

This crashes sometimes. Use CoT to debug it.
```

---

## 3.10 Summary

- CoT makes the model reason before answering.
- "Let's think step by step" is the simplest CoT trigger.
- Few-shot CoT teaches your reasoning format.
- Self-consistency improves reliability for high-stakes answers.
- Don't use CoT for simple tasks — it wastes tokens.

---

*Next: [04-role-prompting.md](./04-role-prompting.md) — System prompts and personas*
