def extract_skills(resume_text):
    skills_database = [
        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "Git",
        "GitHub",
        "HTML",
        "CSS",
        "JavaScript",
        "Docker",
        "AWS",
        "Streamlit"
    ]

    found_skills = []

    resume_lower = resume_text.lower()

    for skill in skills_database:
        if skill.lower() in resume_lower:
            found_skills.append(skill)

    return found_skills