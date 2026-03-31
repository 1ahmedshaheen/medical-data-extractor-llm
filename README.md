# 🏥 AI Medical Data Extraction System

<p align="center">
  <img src="/images/electronic_medical_records.png" width="800"/>
</p>

---

## 🚀 Overview
An AI-powered system that transforms unstructured medical transcripts into structured, machine-readable data using Large Language Models (LLMs).

This project goes beyond simple extraction — it delivers an **interactive AI web application** with real-time processing and analytics.

---

## 🎯 Problem Statement
Medical data is often buried inside unstructured clinical text, making it:
- Hard to analyze 📉
- Difficult to query 🔍
- Impossible to scale 🚫

---

## 💡 Solution
We built an intelligent pipeline that:

1. Reads raw medical transcripts  
2. Uses AI to extract key information  
3. Converts text → structured JSON  
4. Performs validation  
5. Generates analytics & insights  

---

## 🧠 Key Features
- 🤖 LLM-powered data extraction
- 🧪 Demo Mode (no API required)
- 📊 Data analysis & visualization
- 🌐 Interactive Streamlit web app
- ⚡ Real-time processing
- 🔒 Error handling & validation

---

## ⚙️ Tech Stack
- Python
- Pandas
- Streamlit
- OpenAI API (optional)
- Matplotlib

---

## 🔄 Pipeline Workflow
Raw Text → LLM → JSON Extraction → Validation → DataFrame → CSV Output

---

## 🎨 User Interface

| Upload Data | Process | Analyze |
|------------|--------|--------|
| CSV Upload 📂 | AI Extraction 🤖 | Charts 📊 |

---

## ▶️ How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```
### 2. Run The App
```bash
streamlit run app.py```
---

## 📊 Example Input
```bash
Patient is a 45-year-old male complaining of back pain. Recommended treatment includes physical therapy.
```
---

## 📊 Example Output
```bash
{
  "age": 45,
  "recommended_treatment": "Physical therapy"
}
```
---

## 🛡️ Robustness Features
- ✅ JSON validation for  consistency
- ✅ Error handling to API failures
- ✅ Logging system
- ✅ Scalable batch processing

---

## 💡 Use Cases
- Clinical data structuring
- Medical analytics
- Healthcare automation
- AI-powered EHR systems

---

## 👨‍💻 Author
### Ahmed Shaheen
#### AI Engineer | Data Scientist | Computer Vision Enthusiast

---

## ⚠️ Note About API Usage

This project includes a **Demo Mode** that works without an API key.

- By default, the system uses mock outputs for demonstration purposes.
- To enable real AI extraction, set:

```python
USE_API = True

