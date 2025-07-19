from mcq import MCQ
import streamlit as st
import random 
import csv
from PIL import Image




st.cache_data.clear()

logo = Image.open("rpatil.png")

with st.sidebar:
    st.image(logo, width=200)  # Adjust width as needed
    st.write("📭 hastenmminds@gmail.com")

st.title(f"General Science MCQs")



@st.cache_data()
def question_shown():
    questions = []
    with open('questions.csv', newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            mcq = MCQ(
                row["questionID"], 
                row["question"], 
                row["AnswerKey"], 
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            )
            questions.append(mcq)
    return questions

st.subheader("🎯 To Solve: 5")

# Pick 5 random questions
mcqs = question_shown()
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = random.sample(mcqs, 5)

selected = st.session_state.selected_questions

# Initialize answer tracking
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Show all questions and radio buttons
for i, q in enumerate(selected, 1):
    st.markdown(f"**Q{i}:** {q.question}")
    options_list = [q.option1, q.option2, q.option3, q.option4]
    
    # Radio input for each question
    selected_option = st.radio("Choose one:", options_list, key=f"q{i}")
    st.session_state.answers[i] = {
        "selected": selected_option,
        "correct_answer": q.AnswerKey,
        "submitted": False
    }
    st.markdown("---")

# Submit all at once
if st.button("Submit All"):
    for i in range(1, 6):
        st.session_state.answers[i]["submitted"] = True
   

# Show feedback for each question
if any(answer["submitted"] for answer in st.session_state.answers.values()):
    st.subheader("📋 Feedback:")
    for i, q in enumerate(selected, 1):
        ans_info = st.session_state.answers[i]
        selected = ans_info["selected"]
        correct = ans_info["correct_answer"]
        if selected.strip().lower() == correct.strip().lower():
            st.success(f"Q{i}: ✅ Correct")
        else:
            st.error(f"Q{i}: ❌ Incorrect — Correct Answer: **{correct}**")

    if st.button("🔄 New Test"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

