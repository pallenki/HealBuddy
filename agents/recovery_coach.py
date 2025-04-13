from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Default context for all incoming questions
DEFAULT_CONTEXT = (
    "The patient had liposuction surgery 7 days ago and is currently recovering at home. "
    "They are wearing a compression garment and experiencing mild soreness and occasional swelling."
)

def get_response(message: str, context: str = "") -> str:
    full_context = context if context else DEFAULT_CONTEXT

    system_prompt = (
        "You are a friendly and supportive recovery coach helping a patient feel safe, motivated, and informed after liposuction surgery. "
        "Use clear, calming, and encouraging language. Provide non-medical advice only. "
        "Focus on simple actions, daily milestones, comfort tips, and mindset support. "
        "Keep the response to a maximum of 5 short bullet points or lines.\n\n"
        f"Here is the patient context: {full_context}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Recovery Coach GPT Error] {e}"
