import openai
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(user_input: str, context: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a warm, motivational recovery coach helping post-surgery patients stay positive and active."},
                {"role": "user", "content": f"{context}\n\n{user_input}"}
            ]
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"[Recovery Coach GPT Error] {str(e)}"
