# ============================================================
# AI Audit Assistant (Gemini Version)
# ============================================================

import os
from google import genai
from dotenv import load_dotenv

# --- Load environment variables from .env file ---
load_dotenv()

# --- Initialize the Gemini client ---
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# --- The text you want to analyze ---
INPUT_TEXT = """
Our procurement team currently approves vendor payments up to $50,000 
without a second review. The approval process is handled by a single 
manager with no documented checklist. Vendor contracts are stored in 
a shared folder with access granted to all staff. There is no periodic 
review of active vendors, and some vendors have not been evaluated in 
over two years. Staff turnover in the finance department has been high, 
and onboarding documentation is outdated.
"""


def analyze_text(text: str) -> str:
    prompt = f"""
    You are an expert internal auditor. Analyze the following text and 
    respond in EXACTLY this format:

    Summary:
    - [one or two sentence summary]

    Key Risks:
    - [risk 1]
    - [risk 2]
    - [risk 3]

    Recommendations:
    - [recommendation 1]
    - [recommendation 2]
    - [recommendation 3]

    Be concise, professional, and practical.

    Text to analyze:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text


def main():
    print("=" * 50)
    print("       AI AUDIT ASSISTANT")
    print("=" * 50)
    print("\nAnalyzing input text...\n")

    result = analyze_text(INPUT_TEXT)

    print(result)
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()