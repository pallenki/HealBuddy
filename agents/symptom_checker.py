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

def get_gemini_response(message: str, context: str = "") -> str:
    full_context = context if context else DEFAULT_CONTEXT

    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = (
            f"You are a calm and safety-focused symptom checker for post-operative patients recovering from liposuction. "
            f"Do not diagnose. Instead, provide up to 5 clear and supportive bullet points.\n\n"
            f"Patient context: {full_context}\n"
            f"User message: {message}\n\n"
            f"Instructions:\n"
            f"- Limit your response to a maximum of 5 bullet points or short lines.\n"
            f"- Use plain language.\n"
            f"- Always encourage the patient to contact their doctor for anything concerning."
        )

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"[Gemini Error] {e}"
