import requests

BASE_URL = "http://127.0.0.1:8000"


def upload_resume(file):
    files = {
        "file": (file.name, file.getvalue(), "application/pdf")
    }

    response = requests.post(
        f"{BASE_URL}/upload-resume",
        files=files
    )

    return response.json()


def analyze_job(job_text):

    response = requests.post(
        f"{BASE_URL}/analyze-job",
        json={"text": job_text}
    )

    return response.json()


def rank_all():
    response = requests.post(f"{BASE_URL}/rank-all")

    print("Status:", response.status_code)
    print("Response:")
    print(response.text)

    try:
        return response.json()
    except Exception:
        return {"error": response.text}

def reset():

    requests.post(
        f"{BASE_URL}/reset"
    )