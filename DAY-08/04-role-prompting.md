# Module 04 — Role Prompting & Personas

> "The model becomes what you tell it to be. Be precise."

---

## 4.1 What is Role Prompting?

**Role prompting** assigns the model a specific identity, expertise, or persona before giving it a task. This shapes:
- Vocabulary and tone
- Depth of expertise
- Perspective and framing
- What the model pays attention to

### The Mechanism
The model has seen millions of documents written by doctors, lawyers, poets, engineers, and teachers. When you assign a role, you activate that cluster of patterns.

---

## 4.2 Basic Role Assignment

### Simple Role
```
You are a senior Python developer with 10 years of experience.
Explain what a decorator is.
```

vs.

```
Explain what a decorator is.
```

**Difference:** The first produces a precise, technical explanation with real-world use cases. The second may produce something generic.

---

### Role + Audience
```
You are a pediatric doctor explaining a diagnosis to anxious parents.
Explain what "mild anemia" means and what the next steps are.
Use simple language, be reassuring, avoid jargon.
```

**Why it works:** The role anchors the knowledge. The audience anchors the communication style.

---

## 4.3 The System Prompt

In APIs and tools like Claude/ChatGPT, the **system prompt** is a special instruction given BEFORE the conversation. It's the most powerful place to set a role.

### System Prompt Template
```
You are [ROLE] with expertise in [DOMAIN].

Your communication style is [STYLE].

When responding, always [BEHAVIOR].
Never [CONSTRAINT].

Your goal is to [OBJECTIVE].
```

---

### Example: Customer Support Agent
```
SYSTEM PROMPT:
You are a friendly and efficient customer support agent for TechFlow, a SaaS
project management tool. 

Your communication style is warm, empathetic, and solution-focused.

When responding:
- Acknowledge the customer's frustration before solving.
- Provide step-by-step solutions when explaining technical issues.
- Offer to escalate if the issue can't be resolved in 2 exchanges.

Never:
- Blame the customer.
- Admit to system bugs unless confirmed by the engineering team.
- Discuss competitor products.

Your goal is to resolve issues in as few messages as possible while leaving
the customer feeling heard and valued.
```

---

### Example: Code Review Mentor
```
SYSTEM PROMPT:
You are a staff-level software engineer conducting a mentoring code review.

Your style: Direct, educational, and encouraging. Point out issues clearly
but explain WHY something is a problem. Always suggest the better approach.

Format every review as:
🟢 What's good
🟡 What could be improved (with explanation and fix)
🔴 What must be changed (with explanation and fix)

Never rewrite the entire code — teach, don't do it for them.
```

---

## 4.4 Multi-Layered Personas

You can stack multiple dimensions into a role:

```
You are:
- A 15-year veteran Wall Street analyst (expertise)
- Who now teaches at a community college (communication style)  
- Explaining things to first-generation investors (audience)
- Who are skeptical of financial advice (emotional context)

Explain whether index funds are a good investment for someone with $500/month to invest.
```

Each layer narrows the model's response space — you get richer, more targeted output.

---

## 4.5 Perspective Prompting

Ask the model to adopt a specific **viewpoint** to analyze a problem from multiple angles.

### Example: Business Decision
```
I'm considering launching a subscription fitness app.

Analyze this from three perspectives:

1. As a venture capitalist: What makes this fundable or not?
2. As a potential customer: What would make you subscribe or not?
3. As a competitor (existing fitness app): What's your strategic response?

Give each perspective 2-3 bullet points.
```

---

### Example: Debate Technique
```
Topic: "Remote work makes employees less productive."

First, argue FOR this statement as a corporate executive.
Then, argue AGAINST it as a remote employee.
Finally, give your balanced synthesis as an organizational psychologist.
```

---

## 4.6 Expert Panel Prompting

Simulate a room of experts discussing your problem.

```
I need advice on whether to use microservices or a monolith for my new startup.

Simulate a discussion between:
- A startup CTO who scaled a monolith to 10M users
- A DevOps engineer who manages Kubernetes clusters daily
- A solo developer who prefers simplicity

Each person gives their 2-minute take. Then summarize the consensus.
```

---

## 4.7 Role Prompting for Writing Styles

```
Rewrite this product description in the style of:
1. Apple (minimalist, emotional, aspirational)
2. Amazon (feature-rich, benefit-focused, practical)
3. A luxury brand (exclusive, heritage, craftsmanship)

Original: "A bluetooth speaker with 20-hour battery and waterproof design."
```

---

## 4.8 Common Role Prompting Mistakes

### Mistake 1: Vague Role
```
❌ You are an expert. Explain blockchain.
```
"Expert" in what? For whom?

```
✅ You are a blockchain engineer explaining the technology to a CFO
   who understands finance but not computer science.
```

---

### Mistake 2: Role Without Purpose
```
❌ You are Shakespeare. Explain machine learning.
```
Unless you genuinely want Elizabethan prose, the role is decorative noise.

---

### Mistake 3: Conflicting Instructions
```
❌ You are a formal academic writer who uses casual slang and emojis.
```
Contradictions confuse the model. Pick a consistent voice.

---

## 4.9 Role Prompt Templates (Copy-Paste Ready)

### Technical Educator
```
You are a senior [TECHNOLOGY] engineer teaching [TOPIC] to a developer with
[EXPERIENCE_LEVEL] experience. Use clear analogies, real code examples,
and explain the "why" behind each concept.
```

### Business Analyst
```
You are a McKinsey-trained business analyst. When given a business problem,
structure your response using: Situation → Complication → Resolution.
Be concise, data-driven, and always provide 3 options with tradeoffs.
```

### Writing Coach
```
You are a ruthless but kind writing coach. When I share writing, first
identify the strongest sentence, then identify the weakest, then give me
exactly 3 specific improvements. No platitudes.
```

---

## 4.10 Practice Exercises

### Exercise 1
Create a system prompt for an AI tutor that teaches SQL to data analysts who already know Excel.

### Exercise 2
Write a perspective prompt that analyzes a content marketing strategy from the POV of: SEO specialist, social media manager, and sales rep.

### Exercise 3
Design an "expert panel" prompt for deciding between React, Vue, and Svelte for a new project.

---

## 4.11 Summary

- Roles activate domain-specific patterns in the model.
- System prompts are the most powerful place for role instructions.
- Stack: expertise + communication style + audience + constraints.
- Use multi-perspective prompting to get balanced analysis.
- Avoid vague roles, contradictions, and decorative personas.

---

*Next: [05-output-formatting.md](./05-output-formatting.md) — Getting structured output*
