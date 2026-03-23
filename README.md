### **Marketplace ML · Causal Inference · GenAI · Experimentation**

---

### Case

####  Marketplace Pricing ML
> Dynamic pricing · Causal inference · A/B testing · Production ML

End-to-end machine learning project simulating a ride-hailing marketplace (Berlin).
Covers the full lifecycle of a marketplace ML product — EDA, model training,
causal inference, experimentation, and production deployment.

| Notebook | What it covers |
|---|---|
| 01 — EDA | Demand patterns, zone analysis, price elasticity |
| 02 — Dynamic Pricing Model | XGBoost + MLflow + FastAPI + drift monitoring |
| 03 — Causal Inference (DiD) | True voucher effect measurement |
| 04 — A/B Test Evaluation | Experiment design, statistical testing, business recommendation |

**Tech:** Python · XGBoost · MLflow · FastAPI · Docker · DuckDB · Scikit-learn · Causal Inference

**Key concepts demonstrated:**
- Dynamic pricing model served via REST API
- Difference-in-Differences to isolate causal effect of voucher campaigns
- A/B test framework connected to revenue impact, not just p-values
- Model monitoring with data drift detection (KS test)
- Full MLflow experiment tracking

[→ View](https://github.com/fbannayeva/ML-workflow/tree/main/marketplace-pricing-ml)

---

### Analytics LLM Assistant
> RAG · GenAI · Natural language to SQL · Streamlit

A lightweight RAG-based assistant that converts natural-language questions
into SQL queries, executes them locally, and returns plain-English insights —
powered by Google Gemini API (free tier).

**How it works:**
```
Your question
      │
      ▼
Gemini API — reads table schema (RAG) → generates SQL
      │
      ▼
DuckDB — executes SQL locally on CSV
      │
      ▼
Gemini API — explains results in plain English
      │
      ▼
Streamlit UI — SQL + table + insight
```

**Tech:** Python · Gemini API · DuckDB · Streamlit · Docker

**Key concepts demonstrated:**
- RAG pattern — schema context passed to LLM for accurate SQL generation
- Local data processing — CSV never leaves your machine
- Applied GenAI for real analytics tasks, not just chatbots
- Production packaging with Docker

[→ View](https://github.com/fbannayeva/ML-workflow/tree/main/analytics_llm_Gemini)

---

## How the connect

Both projects use the same Berlin ride-hailing dataset (`sample_rides.csv`).
The LLM assistant can query the same data that the pricing model was trained on —
creating a unified analytical environment:
```
sample_rides.csv
      │
      ├──► Marketplace Pricing ML
      │         EDA → Model → Causal Inference → A/B Test
      │
      └──► Analytics LLM Assistant
                Natural language → SQL → Insight
```

---

## Tech Stack

| Category | Tools |
|---|---|
| Languages | Python 3.11, SQL |
| ML / Modelling | Scikit-learn, XGBoost, MLflow |
| Causal Inference | Difference-in-Differences, Bootstrap CI |
| GenAI / LLM | Gemini API, RAG pattern |
| Production | FastAPI, Docker, Streamlit |
| Data Engineering | Pandas, NumPy, DuckDB |
| Visualization | Matplotlib, Seaborn, Plotly |

---

## Status

| Project | Status |
|---|---|
| Marketplace Pricing ML | Complete |
| Analytics LLM Assistant | Complete |
| Geo-spatial extension (H3 grids) | Planned |
| Uplift modelling | Planned |
| Document Q&A Assistant | Planned |

---
## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
Feel free to use, modify, and distribute this work.

**Author:** 
Fidan Bannayeva — [LinkedIn](https://www.linkedin.com/in/fbannaye)

*Portfolio focused on marketplace ML and applied GenAI.
Inspired by real-world challenges at companies like Freenow, Uber, and Bolt.*