"""
Analytics SQL Assistant — powered by Google Gemini API (free tier).
Converts natural-language questions into SQL queries and plain-English insights.

Free tier: 60 requests/minute, 1,500 requests/day — sufficient for portfolio use.
Get your free API key at: https://aistudio.google.com/app/apikey
"""
import os
import duckdb
import pandas as pd
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")  # free tier model


SCHEMA_CONTEXT = """
Table: rides
Columns:
  - timestamp        TIMESTAMP   — ride request time
  - hour             INTEGER     — hour of day (0-23)
  - weekday          INTEGER     — 0=Monday, 6=Sunday
  - is_weekend       INTEGER     — 1 if weekend
  - zone             VARCHAR     — pickup zone name
  - demand_score     FLOAT       — real-time demand index
  - supply_score     FLOAT       — real-time driver supply
  - demand_supply_ratio FLOAT    — demand / supply
  - surge_multiplier FLOAT       — applied price multiplier (1.0 = no surge)
  - base_price_eur   FLOAT       — base fare in EUR
  - final_price_eur  FLOAT       — final fare after surge
  - voucher_applied  INTEGER     — 1 if voucher used
  - voucher_discount_eur FLOAT   — discount amount in EUR
  - conversion       INTEGER     — 1 if ride completed
  - ride_duration_min FLOAT      — trip duration in minutes
"""


def generate_sql(question: str, schema: str = SCHEMA_CONTEXT) -> str:
    """Use Gemini to convert a natural-language question into a SQL query."""
    prompt = f"""You are a SQL expert. Given the following table schema, write a DuckDB-compatible SQL query to answer the question.

Schema:
{schema}

Question: {question}

Rules:
- Return ONLY the SQL query, no explanation, no markdown fences, no backticks.
- Use standard SQL that works in DuckDB.
- Limit results to 20 rows unless the question asks for aggregates.
- Use meaningful column aliases.
"""
    response = model.generate_content(prompt)
    # Strip any accidental markdown fences Gemini sometimes adds
    sql = response.text.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql


def generate_insight(question: str, sql: str, result_df: pd.DataFrame) -> str:
    """Use Gemini to summarise query results in plain English."""
    result_preview = result_df.head(10).to_markdown(index=False)
    prompt = f"""You are a data analyst. A user asked: "{question}"

The SQL query was:
{sql}

The results are:
{result_preview}

Write a concise, clear insight (2-4 sentences) explaining what the data shows.
Focus on the business implication, not technical details.
"""
    response = model.generate_content(prompt)
    return response.text.strip()


def run_query(sql: str, data_path: str = "data/sample_rides.csv") -> pd.DataFrame:
    """Execute SQL against a CSV file using DuckDB."""
    con = duckdb.connect()
    con.execute(f"CREATE TABLE rides AS SELECT * FROM read_csv_auto('{data_path}')")
    result = con.execute(sql).df()
    con.close()
    return result


def answer(question: str, data_path: str = "data/sample_rides.csv") -> dict:
    """
    Full pipeline: question -> SQL -> execute -> insight.

    Returns
    -------
    dict with 'sql', 'result', and 'insight'
    """
    sql     = generate_sql(question)
    result  = run_query(sql, data_path)
    insight = generate_insight(question, sql, result)
    return {"sql": sql, "result": result, "insight": insight}
