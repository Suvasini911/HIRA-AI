from backend.core.gemini_client import ask_gemini
from backend.prompts.resume_prompt import RESUME_PROMPT
from backend.services.local_parser import parse_resume


def extract_candidate_info(text):

    prompt = f"""
{RESUME_PROMPT}

Resume:

{text}
"""

    result = ask_gemini(prompt)

    if result.get("success") == False:
        print("Gemini unavailable. Using Local Parser...")
        return parse_resume(text)

    return result