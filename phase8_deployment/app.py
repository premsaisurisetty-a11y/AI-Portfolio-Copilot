import streamlit as st
from agent_core import generate_response

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(page_title="AI Portfolio Copilot", layout="centered")
st.title("AI Portfolio Copilot - Phase 8 Deployment Wrapper")
st.caption("Decision-support only. No personalized financial advice or guaranteed returns.")

query = st.text_area("Enter user query", height=150)

if st.button("Run Agent"):
    result = generate_response(query)
    st.subheader("Agent Response")
    st.write(result["response"])
    st.metric("Latency", f"{result['latency_ms']} ms")
    st.info(f"Status: {result['status']}")
