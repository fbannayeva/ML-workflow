"""
Streamlit UI for the Analytics SQL Assistant — Gemini version (free).
Run: streamlit run app_gemini.py
"""
import streamlit as st
import pandas as pd
from assistant_gemini import answer, generate_sql, run_query, generate_insight

st.set_page_config(page_title="Analytics Assistant", page_icon="📊", layout="wide")

st.title("📊 Analytics SQL Assistant")
st.caption("Ask questions about ride-hailing data in plain English · Powered by Google Gemini (free)")

EXAMPLE_QUESTIONS = [
    "Which zones had the highest average surge multiplier?",
    "What is the conversion rate by hour of day?",
    "How did vouchers affect conversion compared to non-voucher rides?",
    "What is the average final price on weekends vs weekdays?",
    "Show me the top 5 zones by total rides.",
]

with st.sidebar:
    st.header("Example questions")
    for q in EXAMPLE_QUESTIONS:
        if st.button(q, use_container_width=True):
            st.session_state['question'] = q

    st.divider()
    st.markdown("**Setup**")
    st.markdown("Set your free API key:")
    st.code("export GEMINI_API_KEY=your_key")
    st.markdown("[Get free key →](https://aistudio.google.com/app/apikey)")

question = st.text_input(
    "Your question",
    value=st.session_state.get('question', ''),
    placeholder="e.g. Which zones had the highest surge last weekend?",
)

if st.button("Ask", type="primary") and question:
    with st.spinner("Generating SQL..."):
        sql = generate_sql(question)

    st.subheader("Generated SQL")
    st.code(sql, language="sql")

    with st.spinner("Running query..."):
        try:
            result = run_query(sql)
            st.subheader("Results")
            st.dataframe(result, use_container_width=True)

            with st.spinner("Generating insight..."):
                insight = generate_insight(question, sql, result)
            st.subheader("Insight")
            st.info(insight)

        except Exception as e:
            st.error(f"Query error: {e}")
            st.warning("The SQL might need adjustment. Try rephrasing your question.")
