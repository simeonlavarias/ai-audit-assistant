# 🔍 AI Audit Assistant

A terminal-based Python application that analyzes audit notes, policy documents, or process descriptions using the Google Gemini API. It returns a structured output with a summary, key risks, and actionable recommendations.

---

## 🚀 Features

- Accepts any block of text as input (audit notes, policies, process descriptions)
- Uses Google Gemini AI to analyze the text
- Returns clean, structured output:
  - **Summary**
  - **Key Risks**
  - **Recommendations**
- Securely loads API keys using a `.env` file

---

## 🛠️ Tech Stack

- **Python 3.13**
- **Google Gemini API** (`google-genai`)
- **python-dotenv** for secure environment variable management

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/simeonlavarias/ai-audit-assistant.git
cd ai-audit-assistant
```

### 2. Create and activate a virtual environment
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
Create a `.env` file in the root folder:
```dotenv
GEMINI_API_KEY=your-gemini-api-key-here
```
Get a free API key at: https://aistudio.google.com/apikey

### 5. Run the assistant
```bash
python audit_assistant.py
```

---

## 📋 Example Output

```
==================================================
       AI AUDIT ASSISTANT
==================================================

Analyzing input text...

Summary:
- The procurement process lacks adequate controls, with single-manager
  approvals, unreviewed vendor contracts, and outdated onboarding docs.

Key Risks:
- Unauthorized or fraudulent payments due to lack of dual approval
- Data exposure from unrestricted vendor contract folder access
- Compliance gaps from vendors not reviewed in over two years

Recommendations:
- Implement dual-approval for payments above $10,000
- Restrict contract folder access to relevant roles only
- Schedule bi-annual vendor reviews and update onboarding materials

==================================================
```

---

## 🔮 Future Improvements

- **Accept input from the terminal** — allow users to type or paste text directly instead of editing the source code
- **Save output to a file** — automatically export results to a `.txt` or `.pdf` report
- **Analyze multiple documents** — batch process several files at once
- **Web interface** — add a simple UI using Flask or Streamlit for non-technical users
- **Risk scoring** — assign severity levels (Low / Medium / High) to each identified risk

---

## 🔒 Security Note

This project uses a `.env` file to store the API key. The `.gitignore` is configured to prevent it from being pushed to GitHub.

