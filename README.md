# 🏥 Medical Data Extraction using LLMs

## 🚀 Overview
This project leverages Large Language Models (LLMs) to transform unstructured medical transcripts into structured, machine-readable data.

It extracts key clinical insights such as patient age and recommended treatment using advanced prompt engineering.

---

## 🎯 Problem Statement
Medical data is often stored as unstructured text, making it difficult to analyze, query, or integrate into systems.

This project solves that by converting raw clinical text into structured JSON data.

---

## 🧠 Solution
We use an LLM-powered pipeline to:
1. Read medical transcripts from a CSV file
2. Send each record to an AI model
3. Extract structured fields
4. Validate and store results

---

## ⚙️ Tech Stack
- Python
- Pandas
- OpenAI API (LLMs)
- JSON Processing
- Logging & Error Handling

---

## 🔄 Pipeline Workflow
Raw Text → LLM → JSON Extraction → Validation → DataFrame → CSV Output


---

## ▶️ How to Run

### 1. Install Dependencies
```bash
pip install pandas openai tqdm
API_KEY = "your_api_key"
```
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
✅ JSON validation for  consistency
✅ Error handling to API failures
✅ Logging 
✅ Scalable batch processing

---

## 💡 Use Cases
- Clinical data structuring
- Medical analytics
- Healthcare automation
- AI-powered EHR systems

---

## ⚠️ Note About API Usage

This project includes a **Demo Mode** that works without an API key.

- By default, the system uses mock outputs for demonstration purposes.
- To enable real AI extraction, set:

```python
USE_API = True