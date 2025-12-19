from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Gujarati": "gu",
    "Bengali": "bn",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Arabic": "ar",
    "Japanese": "ja",
    "Korean": "ko"
}

@app.route("/")
def index():
    return render_template("index.html", languages=list(LANGUAGES.keys()))

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    src_name = data.get("src", "English")
    dest_name = data.get("dest", "Hindi")

    src = LANGUAGES.get(src_name, "auto")
    dest = LANGUAGES.get(dest_name, "en")

    if not text.strip():
        return jsonify({"translated_text": ""})

    try:
        translated = GoogleTranslator(source=src, target=dest).translate(text)
        return jsonify({"translated_text": translated})
    except Exception as e:
        return jsonify({"translated_text": f"Error while translating: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
