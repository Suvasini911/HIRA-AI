from backend.core.gemini_client import ask_gemini
from backend.prompts.jd_prompt import JD_PROMPT
from backend.services.local_parser import parse_job


def extract_job_info(text):

    prompt = f"""
{JD_PROMPT}

Job Description:

{text}
"""

    result = ask_gemini(prompt)

    if result.get("success") == False:
        print("Gemini unavailable. Using Local Parser...")
        return parse_job(text)

    return result