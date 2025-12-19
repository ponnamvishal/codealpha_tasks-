# Language Translation Tool

A Flask web application that translates user text between multiple languages using a cloud translation API and provides a simple, user‑friendly interface.

## 🚀 Features

- Translate text from a selected source language to a target language.
- Clean web UI with an input text area and language dropdowns.
- Displays the translated text clearly on the same page.
- Optional extras: copy translated text and text‑to‑speech support (if enabled).

## 🧠 Tech Stack

- Python  
- Flask  
- HTML, CSS (optionally Bootstrap)  
- Translation API (for example Google Translate API / Microsoft Translator API / googletrans library)

## 📂 Project Structure

- `app.py` – Main Flask application and API integration.
- `templates/` – HTML templates for the web interface.
- `static/` – CSS, JavaScript, and other assets.
- `requirements.txt` – Python dependencies.

## ⚙️ Setup & Installation

1. Clone the repository:
   ```
   git clone https://github.com/<ponnamvishal>/codealpha_tasks-.git
   cd codealpha_tasks-/CodeAlpha_Language_Translation_Tool
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

4. Configure your translation API key (if you use a paid API):
   - Create a `.env` or `config.py` file.
   - Store the API key there and load it in `app.py`.

## ▶️ Running the App

```
python app.py
```

Then open `http://127.0.0.1:5000` in your browser and start translating text.

## 🌐 How It Works

1. User enters text and selects source and target languages in the form.
2. Flask receives the request and calls the translation API/library with the text and language codes.
3. The translated text is returned and rendered on the result section of the page.

## 🎯 Learning Outcomes

- Building a small full‑stack Flask application.
- Consuming external translation APIs from Python.
- Handling forms, routes, and template rendering in Flask.
```