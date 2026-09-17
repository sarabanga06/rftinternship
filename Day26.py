import streamlit as st
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("📄 AI Resume Screening Tool")

skills = [
    "python","java","sql","html","css","javascript","react",
    "pandas","numpy","machine learning","deep learning",
    "scikit-learn","power bi","tableau","excel","git",
    "communication","leadership","problem solving","teamwork"
]

def get_skills(text):
    text = text.lower()
    return [s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", text)]

def get_name(text, file):
    lines = [x.strip() for x in text.split("\n") if x.strip()]
    return lines[0] if lines else file

files = st.file_uploader(
    "Upload Resumes (TXT/CSV)",
    type=["txt", "csv"],
    accept_multiple_files=True
)

job = st.text_area(
    "Enter Job Description",
    "Python SQL Pandas NumPy Machine Learning Power BI "
    "Data Analysis Communication Problem Solving"
)

threshold = st.slider("Shortlist Score", 0, 100, 50)

if files:

    candidates = []

    for file in files:

        if file.name.endswith(".txt"):
            text = file.read().decode("utf-8")
            name = get_name(text, file.name)

        else:
            data = pd.read_csv(file)
            text = " ".join(data.astype(str).values.flatten())
            name = data.iloc[0].get("Name", file.name)

        candidates.append({
            "Name": name,
            "Text": text,
            "Skills": get_skills(text)
        })

    documents = [job] + [x["Text"] for x in candidates]

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)

    scores = cosine_similarity(
        matrix[0:1], matrix[1:]
    )[0] * 100

    job_skills = set(get_skills(job))
    results = []

    for candidate, score in zip(candidates, scores):

        candidate_skills = set(candidate["Skills"])

        results.append({
            "Name": candidate["Name"],
            "Match Score": round(score, 2),
            "Matched Skills": ", ".join(
                candidate_skills & job_skills
            ),
            "Missing Skills": ", ".join(
                job_skills - candidate_skills
            ),
            "Shortlisted": score >= threshold
        })

    result = pd.DataFrame(results)
    result = result.sort_values(
        "Match Score",
        ascending=False
    ).reset_index(drop=True)

    result.insert(0, "Rank", range(1, len(result) + 1))

    st.subheader("🏆 Candidate Ranking")
    st.dataframe(result, use_container_width=True)

    st.subheader("⚠️ Missing Skills")

    for _, row in result.iterrows():
        st.write(
            f"**{row['Name']}** → "
            f"{row['Missing Skills'] or 'None'}"
        )

    st.subheader("✅ Shortlisted Candidates")

    shortlisted = result[
        result["Shortlisted"]
    ]

    st.dataframe(
        shortlisted,
        use_container_width=True
    )

    st.download_button(
        "⬇️ Download Results",
        result.to_csv(index=False),
        "shortlisted_candidates.csv",
        "text/csv"
    )