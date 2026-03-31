# =========================================
# 🏥 AI Data Extraction & Smart Analytics App
# =========================================

import streamlit as st
import pandas as pd
import numpy as np
import json
import logging
from tqdm import tqdm
import matplotlib.pyplot as plt

# =========================================
# ⚙️ Config
# =========================================
USE_API = False  # Demo mode (no API)

logging.basicConfig(level=logging.INFO)

st.set_page_config(page_title="AI Data Analyzer", layout="wide")

# =========================================
# 🧠 AI Extraction (Generic لأي نص)
# =========================================
def extract_info(text):
    if not USE_API:
        return {
            "detected_number": np.random.randint(20, 60),
            "detected_category": "sample_category"
        }

# =========================================
# 🎨 UI Header
# =========================================
st.title("🤖 AI Data Analyzer & Extractor")
st.markdown("Upload **any CSV file** and get **AI insights + analytics + visualization**")

# =========================================
# 📂 File Upload
# =========================================
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully")

    st.subheader("📊 Raw Data Preview")
    st.dataframe(df.head())

    # =========================================
    # 🔍 Detect Text Columns Automatically
    # =========================================
    text_columns = df.select_dtypes(include=["object"]).columns.tolist()
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

    st.write("### 🔍 Detected Columns")
    st.write(f"Text Columns: {text_columns}")
    st.write(f"Numeric Columns: {numeric_columns}")

    # =========================================
    # 🚀 Processing
    # =========================================
    if st.button("🚀 Run AI Processing"):

        results = []

        progress = st.progress(0)

        for i, row in enumerate(df.itertuples(index=False)):

            combined_text = " ".join([str(getattr(row, col)) for col in text_columns])

            extracted = extract_info(combined_text)

            results.append(extracted)

            progress.progress((i + 1) / len(df))

        ai_df = pd.DataFrame(results)

        final_df = pd.concat([df, ai_df], axis=1)

        # =========================================
        # 📊 Results
        # =========================================
        st.subheader("📊 Processed Data")
        st.dataframe(final_df)

        # =========================================
        # 📥 Download
        # =========================================
        csv = final_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Download Processed Data",
            csv,
            "processed_data.csv",
            "text/csv"
        )

        # =========================================
        # 📊 SMART EDA
        # =========================================
        st.subheader("📊 Smart Data Analysis")

        col1, col2 = st.columns(2)

        # ---------------------------
        # 📈 Numeric Analysis
        # ---------------------------
        if numeric_columns:

            with col1:
                st.write("### 📈 Numeric Statistics")
                st.write(final_df[numeric_columns].describe())

                for col in numeric_columns:
                    st.write(f"### 📊 Distribution of {col}")

                    fig, ax = plt.subplots()
                    final_df[col].dropna().hist(ax=ax)
                    st.pyplot(fig)

        # ---------------------------
        # 📊 Categorical Analysis
        # ---------------------------
        if text_columns:

            with col2:
                st.write("### 📊 Categorical Insights")

                for col in text_columns:
                    st.write(f"### 🔹 Top Values in {col}")

                    counts = final_df[col].value_counts().head(10)
                    st.bar_chart(counts)

        # =========================================
        # 🔥 Correlation Matrix
        # =========================================
        if len(numeric_columns) > 1:
            st.write("### 🔥 Correlation Matrix")

            corr = final_df[numeric_columns].corr()

            fig, ax = plt.subplots()
            cax = ax.matshow(corr)
            plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
            plt.yticks(range(len(corr.columns)), corr.columns)

            st.pyplot(fig)

        # =========================================
        # 🧠 Auto Insights
        # =========================================
        st.subheader("🧠 Auto Insights")

        insights = []

        for col in numeric_columns:
            insights.append(f"Average of {col}: {round(final_df[col].mean(), 2)}")

        for col in text_columns:
            most_common = final_df[col].mode()[0] if not final_df[col].mode().empty else "N/A"
            insights.append(f"Most common value in {col}: {most_common}")

        for ins in insights:
            st.write("•", ins)

else:
    st.info("👆 Upload a CSV file to start")