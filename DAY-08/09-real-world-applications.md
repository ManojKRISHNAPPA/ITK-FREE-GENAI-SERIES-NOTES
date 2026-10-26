# Module 09 — Real-World Applications

> "Prompt engineering is not abstract. These are the exact patterns used in production."

---

## 9.1 Software Development

### Code Generation
```
Write a Python function that:
- Accepts a list of dictionaries (each with 'name', 'age', 'score')
- Filters out anyone under 18
- Returns the top 5 by score, sorted descending
- Returns an empty list if input is empty or None

Requirements:
- Include type hints
- Raise ValueError for invalid input types
- Include a docstring
- No external libraries

Write the function, then write 3 pytest test cases covering edge cases.
```

---

### Code Review
```
Review the following Python code as a senior engineer.

Code:
```python
def get_user(id):
    conn = db.connect()
    result = conn.execute("SELECT * FROM users WHERE id = " + str(id))
    return result.fetchone()
```

Check for:
1. Security vulnerabilities
2. Error handling gaps
3. Performance issues
4. Code style / best practices

For each issue: name it, explain why it's a problem, and show the fix.
```

---

### Debugging Prompt
```
I have a bug. Here is my code and the error:

Code:
[paste code]

Error:
[paste error message and stack trace]

What I expected: [describe expected behavior]
What actually happens: [describe actual behavior]

Diagnose the root cause. Don't just fix the surface error — tell me WHY it's failing.
Then show me the corrected code.
```

---

### Writing Unit Tests
```
Here is a function:
[paste function]

Write comprehensive pytest unit tests for this function.
Cover:
- Happy path (normal inputs)
- Edge cases (empty, None, boundary values)
- Error cases (invalid inputs)
- At least one parametrize decorator for multiple similar cases

Use descriptive test names that explain what's being tested.
```

---

## 9.2 Data Analysis

### Analyzing a Dataset Description
```
Here is a description of a dataset:

Columns: user_id, signup_date, last_active_date, plan (free/pro/enterprise),
         monthly_revenue, country, referral_source

I want to understand user churn patterns.

Suggest:
1. The 5 most important analyses to run
2. The SQL query for each analysis
3. What insight each query is designed to reveal

Assume PostgreSQL.
```

---

### Interpreting Data Results
```
Here are the results of a user retention analysis:

Week 1: 100% (baseline)
Week 2: 62%
Week 4: 41%
Week 8: 28%
Week 12: 21%

Context: SaaS product, average plan price $29/month, mostly small business customers.

Analyze this retention curve:
- Is this good, average, or poor for this type of product?
- What do the drop-off points suggest?
- What are the top 3 hypotheses for why users churn?
- What experiments would you run to improve retention?
```

---

### Data Cleaning Instructions
```
I have a CSV with a 'phone_number' column that contains inconsistent formats:
+1 (555) 123-4567
555-123-4567
15551234567
(555)123.4567

Write a Python function using regex that normalizes all of these to:
+1XXXXXXXXXX (E.164 format)

Handle edge cases: missing country code (assume US), invalid numbers.
```

---

## 9.3 Content & Marketing

### SEO Blog Post
```
Write an SEO-optimized blog post about [TOPIC].

Target keyword: "[primary keyword]"
Secondary keywords: "[kw1]", "[kw2]", "[kw3]"
Target audience: [description]
Search intent: Informational (the reader wants to learn, not buy)
Word count: 1,200–1,500 words

Structure:
- Hook opening (question or surprising stat)
- H2 sections (5–6 sections)
- Practical tips in each section
- FAQ section (3 questions from related searches)
- CTA at the end

Tone: Authoritative but accessible. No jargon without explanation.
```

---

### Ad Copy (A/B Testing)
```
Write 3 versions of Facebook ad copy for [PRODUCT/SERVICE].

Target audience: [description]
Key benefit: [main value proposition]
Offer: [discount/trial/free shipping]

Each version should use a different psychological approach:
Version A: Social proof (use numbers, testimonials)
Version B: Fear of missing out / urgency
Version C: Curiosity / question hook

For each version:
- Headline (max 40 chars)
- Primary text (max 125 chars)
- Call to action button text (1-4 words)
```

---

### Email Subject Line Testing
```
I'm sending an email to our newsletter subscribers about [topic].

Write 10 subject line variations testing:
- Curiosity gap
- Numbers/lists ("5 ways to...")
- Question format
- Direct benefit statement
- Urgency
- Personalization hook
- Controversial angle

For each, predict the likely open rate impact: Low / Medium / High
and explain why in one sentence.
```

---

## 9.4 Research & Analysis

### Literature Review Helper
```
I'm researching [TOPIC] for [PURPOSE].

Here is a research paper abstract:
[paste abstract]

Analyze this paper for me:
1. What is the core claim?
2. What methodology did they use?
3. What are the key findings?
4. What are the limitations the authors acknowledge?
5. How does this relate to the question: [your research question]?
6. What follow-up questions does this raise?

Do not speculate beyond what's in the abstract.
```

---

### Competitive Analysis
```
I'm analyzing [COMPANY] as a competitor.

Using publicly available information patterns you've been trained on,
analyze them across:

1. Business Model (how they make money)
2. Target Customer (who they serve)
3. Key Differentiators (what makes them unique)
4. Weaknesses (what they do poorly or what customers complain about)
5. Recent Strategic Moves (last 12-18 months if known)

Note your confidence level for each section: [HIGH/MEDIUM/LOW]
Flag any areas where I should do additional primary research.
```

---

## 9.5 Education & Learning

### Concept Explainer (Feynman Technique)
```
Explain [CONCEPT] to me using the Feynman Technique:
1. Explain it simply, as if to a bright 12-year-old.
2. Identify the parts of the explanation that require deeper knowledge.
3. Explain those parts more deeply, but still simply.
4. Give me one analogy from everyday life.
5. Give me one concrete example of it in the real world.
```

---

### Study Guide Generator
```
I'm studying for an exam on [SUBJECT/CHAPTER].

Create a study guide that includes:
1. Key concepts (list of 10–15 terms with 1-sentence definitions)
2. Concept map (show how ideas connect, text format)
3. Common exam question types for this subject
4. 5 practice questions with answers
5. The 3 most commonly misunderstood concepts and why they trip students up
```

---

### Socratic Tutor
```
I want to learn [CONCEPT] through the Socratic method.

Ask me a series of questions — one at a time — that lead me to discover
the concept myself. Don't give me the answer. 

If I'm wrong, ask another question that helps me see my error.
If I'm stuck, give me a small hint, not the answer.

Start with the first question.
```

---

## 9.6 Business Operations

### Meeting Summary
```
Here are my raw meeting notes:
[paste notes]

Convert these into a structured meeting summary:

# Meeting: [extract topic]
**Date:** [extract if available]
**Attendees:** [extract if mentioned]

## Decisions Made
[bullet list]

## Action Items
| Owner | Task | Deadline |
|-------|------|----------|

## Open Questions
[bullet list]

## Next Meeting Topics
[bullet list]
```

---

### Job Description Generator
```
Create a job description for a [ROLE] at a [COMPANY TYPE/SIZE].

Requirements:
- Team: [team name/size]
- Reports to: [title]
- Key responsibilities: [paste rough notes]
- Must-have skills: [list]
- Nice-to-have skills: [list]
- Culture values: [list]

Format:
- Compelling opening paragraph (why this role matters)
- Responsibilities (5–7 bullets)
- Requirements (split into Must Have and Nice to Have)
- What we offer (benefits, growth, culture)
- Closing sentence with application instructions

Tone: [startup/corporate/technical/creative]
```

---

## 9.7 Personal Productivity

### Weekly Planning
```
Here are my goals and tasks for this week:

Goals: [list]
Tasks (unorganized): [dump of everything]
Constraints: [meetings, deadlines, energy patterns]

Help me:
1. Prioritize using Eisenhower Matrix (Urgent/Important)
2. Identify tasks to delegate or eliminate
3. Create a Mon–Fri daily schedule with time blocks
4. Flag any unrealistic expectations in my list
```

---

### Learning Roadmap
```
I want to learn [SKILL/TOPIC] in [TIMEFRAME].

My current level: [beginner/intermediate/advanced]
My goal: [what I want to be able to do]
Time available: [hours per week]
Learning style: [reading/videos/projects/courses]

Create:
1. A phased learning roadmap (Phase 1 / 2 / 3)
2. Specific resources for each phase (type of resource, not URLs)
3. A mini-project for each phase to apply the learning
4. Milestones to measure progress
5. Warning: what most people get wrong when learning this
```

---

## 9.8 Summary

Real-world prompt engineering is about:
- **Specificity** — the more context you give, the better the output.
- **Structure** — define what you need in each section.
- **Iteration** — first prompt is a draft, not a final product.
- **Domain vocabulary** — use the right terms for your field.
- **Constraints** — always bound the output (length, format, scope).

---

*Next: [10-expert-patterns.md](./10-expert-patterns.md) — Production prompts, evaluation, and mastery*
