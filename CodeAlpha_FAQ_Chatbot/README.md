#  FAQ Chatbot

An FAQ chatbot that answers common questions by matching user input with the most similar frequently asked question using NLP preprocessing and cosine similarity.

## 🚀 Features

- Loads a curated FAQ dataset (questions and answers) from a JSON file.
- Preprocesses text (lowercasing, removing punctuation/stopwords, tokenization).
- Uses TF‑IDF vectorization and cosine similarity to find the closest FAQ to a user query.
- Returns a fallback response when no good match is found.
- Web interface with Flask and (optionally) a simple desktop version.

## 🧠 Tech Stack

- Python  
- Flask  
- scikit‑learn (TF‑IDF Vectorizer, cosine similarity)  
- NLTK / spaCy for basic NLP preprocessing  

## 📂 Project Structure

- `faq_data.json` – FAQ questions and answers.  
- `faq_chatbot/faq_web_app.py` – Flask web chatbot.  
- `faq_chatbot/faq_desktop_app.py` – Desktop chatbot (optional).  
- `faq_chatbot/templates/` – HTML templates for the chat UI.  
- `faq_chatbot/static/` – CSS and JS assets.  
- `requirements.txt` – Python dependencies.  

## ⚙️ Setup & Installation

1. Clone the repository:
   ```
   git clone https://github.com/<ponnamvishal>/codealpha_tasks-.git
   cd codealpha_tasks-/CodeAlpha_FAQ_Chatbot
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux / macOS
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## ▶️ Running the Chatbot (Web)

```
cd faq_chatbot
python faq_web_app.py
```

Open `http://127.0.0.1:5000` in your browser to chat with the FAQ bot.

### Desktop version (optional)

```
python faq_desktop_app.py
```
## 🧮 How It Works

1. Preprocess user queries and FAQ questions (cleaning and tokenization).  
2. Convert all texts into TF‑IDF vectors.  
3. Compute cosine similarity between the user query vector and each FAQ vector.  
4. Return the answer of the FAQ with the highest similarity score, or a fallback message if the score is below a threshold.   

## 🎯 Learning Outcomes

- Implementing a retrieval‑based chatbot using classical NLP.  
- Working with TF‑IDF and cosine similarity for text similarity.  
- Building both web and desktop interfaces around the same chatbot logic.  