import json
import google.generativeai as genai

from backend.config import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)


def ask_gemini(prompt):

    try:

        response = model.generate_content(prompt)

        answer = response.text

        answer = answer.replace("```json", "")
        answer = answer.replace("```", "")

        answer = answer.strip()

        return json.loads(answer)

    except Exception as e:

        return {
            "error": str(e)
        }