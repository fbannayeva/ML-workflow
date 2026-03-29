# Analytics SQL Assistant — LLM / GenAI 

A lightweight RAG-based assistant that generates SQL queries and data insights
from natural-language questions, powered by Google Gemini API (free tier).

## What it does

- Accepts plain-language questions about your data
  ("Which zones had the highest surge last weekend?")
- Generates correct SQL queries using table schema as context (RAG pattern)
- Executes SQL locally on your CSV file via DuckDB — data never leaves your machine
- Returns results + a plain-English summary of the findings
- Runs as a Streamlit app, containerised with Docker

## Architecture
```
User question
      │
      ▼
Schema context (RAG — table structure passed to model)
      │
      ▼
Gemini API ──► SQL query generated
      │
      ▼
DuckDB (local) ──► executes SQL on sample_rides.csv
      │
      ▼
Gemini API ──► plain-English insight
      │
      ▼
Streamlit UI — shows SQL + results + insight
```

## Tech Stack

- **LLM:** Google Gemini API (gemini-1.5-flash, free tier)
- **Pattern:** RAG (Retrieval-Augmented Generation)
- **SQL engine:** DuckDB (in-memory, runs on CSV locally)
- **UI:** Streamlit
- **Container:** Docker

## Setup

### Option 1 — Run locally
```bash
# 1. Get free API key at https://aistudio.google.com/app/apikey

# 2. Install dependencies
pip3 install -r requirements_gemini.txt

# 3. Add your data
# Place sample_rides.csv in the data/ folder

# 4. Set API key (temporary, disappears when terminal closes)
export GEMINI_API_KEY=your_key_here

# 5. Run
streamlit run app_gemini.py
```

### Option 2 — Docker
```bash
docker build -t llm-assistant .
docker run -p 8501:8501 -e GEMINI_API_KEY=your_key llm-assistant
```

Open browser at `http://localhost:8501`

## Example questions
```
"Which zones had the highest surge multiplier?"
"What is the conversion rate by hour of day?"
"How did vouchers affect conversion vs non-voucher rides?"
"What is the average price on weekends vs weekdays?"
"Show me the top 5 zones by total rides."
```

## Example output
```
Question: "Which zones had the highest surge on weekends?"

Generated SQL:
  SELECT zone,
         AVG(surge_multiplier) AS avg_surge,
         COUNT(*)              AS total_rides
  FROM rides
  WHERE is_weekend = 1
  GROUP BY zone
  ORDER BY avg_surge DESC

Insight: Mitte and Kreuzberg had the highest average surge on weekends
(1.8x and 1.6x respectively), driven by leisure demand concentrated
in central Berlin zones on Saturday and Sunday evenings.
```

## Data privacy

- `sample_rides.csv` is processed **locally** by DuckDB — never sent to any API
- Only the question, table schema, and a 10-row result preview are sent to Gemini
- API key is stored only in the terminal session — disappears when terminal closes
- All data in this project is **synthetic** — no real user data

## What this demonstrates

| Concept | Implementation |
|---|---|
| RAG pattern | Table schema passed as context in every prompt |
| LLM for structured output | Gemini generates valid DuckDB SQL |
| Local data processing | DuckDB executes queries on CSV |
| GenAI for insight generation | Gemini explains results in plain English |
| Production packaging | Streamlit UI + Docker deployment |

## Status

Complete — runs locally and in Docker.

---
*Part of a case focused on applied GenAI for data analytics.
Companion project to [marketplace-pricing-ml](https://github.com/yourname/marketplace-pricing-ml).*

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
Feel free to use, modify, and distribute this work.


