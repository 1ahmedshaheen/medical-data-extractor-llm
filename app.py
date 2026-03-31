import streamlit as st
import pandas as pd
import json
import logging
from tqdm import tqdm

# =========================
# ⚙️ Config
# =========================
USE_API = False  # خليه False عشان معندكش API

# =========================
# 🧠 Prompt
# =========================
SYSTEM_PROMPT = """
Extract:
- age
- recommended_treatment

Return JSON only.
"""

# =========================
# 🧪 Mock Function
# =========================
def extract_info(text):
    if not USE_API:
        return {
            "age": 30,
            "recommended_treatment": "General check-up"
        }

# =========================
# 🎨 UI
# =========================
st.set_page_config(page_title="Medical Extractor", layout="wide")

st.title("🏥 Medical Data Extractor (AI)")

st.write("Upload a CSV file with a 'transcription' column")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "transcription" not in df.columns:
        st.error("CSV must contain 'transcription' column")
    else:
        st.success("File loaded successfully ✅")

        if st.button("🚀 Process Data"):
            results = []

            progress_bar = st.progress(0)

            for i, text in enumerate(df["transcription"]):
                results.append(extract_info(text))
                progress_bar.progress((i + 1) / len(df))

            result_df = pd.DataFrame(results)
            final_df = pd.concat([df, result_df], axis=1)

            st.subheader("📊 Results")
            st.dataframe(final_df)

            csv = final_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇️ Download Results",
                csv,
                "results.csv",
                "text/csv"
            )