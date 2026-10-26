# Module 05 — Output Formatting

> "The right answer in the wrong format is still wrong."

---

## 5.1 Why Output Format Matters

LLMs produce text. But you often need that text in a specific shape — JSON for an API, a table for a report, a bullet list for a slide, or code for a script.

If you don't specify format, the model guesses. Usually it guesses wrong.

**Rule:** Always tell the model exactly what format you want.

---

## 5.2 Plain Text Formatting

### Bullet Points
```
List the top 5 benefits of exercise.
Format: bullet points, one benefit per line, maximum 10 words each.
```

### Numbered Lists
```
Give me a step-by-step guide to deploy a Node.js app on AWS EC2.
Format: numbered steps. Include a sub-step where needed.
```

### Headings and Sections
```
Write a product comparison between Notion and Obsidian.
Structure:
- Overview (2 sentences each)
- Key Features (3 bullets each)
- Best For (1 sentence each)
- Verdict (1 paragraph)
```

---

## 5.3 Table Format

Tables are great for comparisons, feature lists, and structured data.

### Example: Technology Comparison
```
Compare PostgreSQL, MySQL, and MongoDB across these dimensions:
- Type (SQL/NoSQL)
- Best use case
- Scalability (1-5)
- Learning curve (Easy/Medium/Hard)

Format: Markdown table with a header row.
```

**Expected Output:**
```markdown
| Database   | Type   | Best Use Case          | Scalability | Learning Curve |
|------------|--------|------------------------|-------------|----------------|
| PostgreSQL | SQL    | Complex queries, analytics | 4/5      | Medium         |
| MySQL      | SQL    | Web applications       | 3/5         | Easy           |
| MongoDB    | NoSQL  | Flexible/document data | 5/5         | Medium         |
```

---

## 5.4 JSON Output

JSON is essential for using LLM output in code.

### Basic JSON Request
```
Extract the following information from this job posting and return it as JSON:
- job_title
- company
- location (city, country)
- salary_range (min, max, currency)
- required_skills (array)
- is_remote (boolean)

Job Posting:
"Senior Python Developer at DataCo in Berlin, Germany. Salary: €70,000–€90,000.
Must know Python, Django, PostgreSQL. Hybrid remote OK."

Return only valid JSON. No explanation.
```

**Expected Output:**
```json
{
  "job_title": "Senior Python Developer",
  "company": "DataCo",
  "location": {
    "city": "Berlin",
    "country": "Germany"
  },
  "salary_range": {
    "min": 70000,
    "max": 90000,
    "currency": "EUR"
  },
  "required_skills": ["Python", "Django", "PostgreSQL"],
  "is_remote": true
}
```

---

### JSON with Schema
For stricter control, provide the JSON schema:

```
Analyze this customer review and return JSON matching this schema:

{
  "sentiment": "positive" | "negative" | "neutral",
  "score": 1-10,
  "key_topics": [string],
  "action_required": boolean,
  "suggested_response_tone": "apologetic" | "informational" | "celebratory"
}

Review: "The onboarding was confusing but once I figured it out, the product
is fantastic. Would love better documentation though."
```

---

## 5.5 XML Output

XML is preferred in some enterprise systems and is excellent for nested data.

```
Parse this address and return it in XML:

"123 Main Street, Apt 4B, Chicago, Illinois, 60601, USA"
```

**Expected Output:**
```xml
<address>
  <street>123 Main Street</street>
  <unit>Apt 4B</unit>
  <city>Chicago</city>
  <state>Illinois</state>
  <zip>60601</zip>
  <country>USA</country>
</address>
```

---

## 5.6 Code Output

### Specifying Language
```
Write a function in Python that:
- Takes a list of dictionaries
- Each dict has 'name' and 'score' keys
- Returns the top 3 by score as a sorted list

Include type hints and a docstring.
```

### Specifying Style
```
Write the same function in JavaScript using:
- Arrow functions
- Array destructuring
- No external libraries
- JSDoc comments
```

### Specifying Code + Explanation
```
Write a Redis caching decorator in Python.

Format your response as:
1. The code (in a ```python block)
2. A line-by-line explanation
3. One example of how to use it
```

---

## 5.7 Structured Report Format

```
Analyze the following business metrics and produce a weekly report.

Data:
- Revenue: $45,200 (up 12% from last week)
- New signups: 342 (down 8%)
- Churn: 2.1% (up 0.3%)
- NPS: 67 (unchanged)

Format your report as:

# Weekly Business Report — [Date]

## Executive Summary
[2-3 sentences]

## Key Metrics
[Table]

## Wins This Week
[2-3 bullets]

## Concerns
[2-3 bullets with severity: High/Medium/Low]

## Recommended Actions
[Numbered list, max 3]
```

---

## 5.8 Constrained Length Formats

### The "Tweet" Format
```
Summarize the main argument of this article in a single tweet (max 280 characters,
no hashtags):

[article text]
```

### The "Elevator Pitch" Format
```
Explain quantum computing as a 30-second elevator pitch to a potential investor.
Max 75 words. End with a hook question.
```

### The "TLDR" Format
```
Read the following text and provide:
- TLDR (1 sentence)
- Key Points (3 bullets)
- What to Do Next (1 action item)

Text: [your text]
```

---

## 5.9 Controlling Format Consistency

When running multiple completions or in a pipeline, you need reliable formats.

### Technique 1: "Return ONLY..."
```
Return ONLY the JSON. No explanation, no markdown code blocks, no preamble.
```

### Technique 2: Show the Start
```
Begin your response with:
{
  "analysis":
```

Starting the model's output locks it into the format.

### Technique 3: Negative Constraints
```
Do NOT include:
- Introductory sentences like "Certainly!" or "Here is..."
- Trailing notes or disclaimers
- Markdown formatting (no ** or ##)
```

---

## 5.10 Format Cheat Sheet

| You Need | Tell the Model |
|----------|---------------|
| JSON | "Return as JSON. No other text." |
| Table | "Format as a Markdown table with columns: X, Y, Z" |
| Bullet list | "Return as bullet points. Max 10 words each." |
| Code only | "Return only the code. No explanation." |
| Short answer | "Answer in one sentence / max N words." |
| Structured sections | "Use these headings: [H1, H2, H3]" |
| No fluff | "Do not include greetings or closing remarks." |

---

## 5.11 Practice Exercises

### Exercise 1
Write a prompt that extracts all product names, prices, and availability from a paragraph of text and returns clean JSON.

### Exercise 2
Create a prompt that produces a 2x2 decision matrix comparing two job offers (salary, growth, work-life balance, stability) as a Markdown table.

### Exercise 3
Write a prompt that generates a weekly standup update from a list of raw bullet points in this format:
- What I did (3 bullets)
- What I'll do next (2 bullets)
- Blockers (1 bullet or "None")

---

## 5.12 Summary

- Always specify the format you want — never assume.
- JSON is the most useful format for programmatic use.
- Use "Return ONLY..." to avoid preamble/postamble noise.
- Tables are ideal for comparisons.
- Constrain length explicitly (words, sentences, bullets).

---

*Next: [06-advanced-techniques.md](./06-advanced-techniques.md) — ReAct, Tree of Thought, and beyond*
