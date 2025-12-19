from flask import Flask, render_template, request, jsonify
import json
import string

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data once
nltk.download("punkt")
nltk.download("stopwords")

app = Flask(__name__)

# ------------- FAQ + NLP SETUP -------------

with open("faq_data.json", "r", encoding="utf-8") as f:
    FAQ_DATA = json.load(f)


QUESTIONS = [item["question"] for item in FAQ_DATA]
ANSWERS = [item["answer"] for item in FAQ_DATA]

STOP_WORDS = set(stopwords.words("english"))

def preprocess(text: str) -> str:
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [
        t for t in tokens
        if t not in STOP_WORDS and t not in string.punctuation
    ]
    return " ".join(tokens)

preprocessed_questions = [preprocess(q) for q in QUESTIONS]
VECTORIZER = TfidfVectorizer()
FAQ_MATRIX = VECTORIZER.fit_transform(preprocessed_questions)

SIM_THRESHOLD = 0.3

def get_best_answer(user_question: str) -> str:
    if not user_question.strip():
        return "Please type a question."
    processed = preprocess(user_question)
    user_vec = VECTORIZER.transform([processed])
    sims = cosine_similarity(user_vec, FAQ_MATRIX)[0]
    best_index = sims.argmax()
    best_score = sims[best_index]
    if best_score >= SIM_THRESHOLD:
        return ANSWERS[best_index]
    return "Sorry, I could not find a matching answer."

# ------------- FLASK ROUTES -------------

@app.route("/")
def index():
    return render_template("faq_index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    reply = get_best_answer(user_msg)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
