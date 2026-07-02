import re

COMMON_SKILLS = [
    "python","java","c","c++","sql","mongodb","mysql","fastapi","flask",
    "django","react","nodejs","aws","docker","git","github",
    "machine learning","deep learning","ai","artificial intelligence",
    "pandas","numpy","scikit-learn","tensorflow","streamlit"
]

def parse_resume(text):

    text_lower = text.lower()

    skills = []

    for skill in COMMON_SKILLS:
        if skill.lower() in text_lower:
            skills.append(skill)

    email = ""

    m = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    if m:
        email = m.group()

    phone = ""

    m = re.search(r'(\+?\d[\d\s-]{8,15})', text)

    if m:
        phone = m.group().strip()

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    name = "Unknown Candidate"

    for line in lines:
      if len(line.split()) >= 2 and "@" not in line and len(line) < 40:
        name = line
        break

    return {

        "personal":{

            "name":name,

            "email":email,

            "phone":phone

        },

        "skills":{

            "programming":skills,

            "frameworks":[],

            "databases":[],

            "cloud":[],

            "ai_ml":[],

            "tools":[],

            "soft_skills":[]

        }

    }


def parse_job(text):

    text=text.lower()

    mandatory=[]

    for skill in COMMON_SKILLS:

        if skill in text:

            mandatory.append(skill)

    return{

        "mandatory_skills":mandatory
    }