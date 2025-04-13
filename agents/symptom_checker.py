import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Default context for liposuction patient
DEFAULT_CONTEXT = (
    "The patient had liposuction surgery 7 days ago and is currently recovering at home. "
    "They are wearing a compression garment and experiencing mild soreness and occasional swelling."
)

def get_response(message: str, context: str = "") -> str:
    full_context = context if context else DEFAULT_CONTEXT

    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = (
            f"You are a safety-focused symptom checker for post-operative patients. "
            f"Do not diagnose, but flag symptoms that may need follow-up. "
            f"Speak clearly and calmly.\n\n"
            f"Patient context: {full_context}\n"
            f"User message: {message}\n"
            f"Provide a supportive and clear response."
        )

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"[Gemini Error] {e}"
