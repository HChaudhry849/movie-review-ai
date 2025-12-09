from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import joblib
from pathlib import Path

app = Flask(__name__)
CORS(app)  # Enable CORS

# Dynamically find the project root
ROOT_DIR = Path(__file__).resolve().parents[2]  # app.py is in root, adjust if inside another folder
MODELS_DIR = ROOT_DIR / "models"

MODEL_PATH = MODELS_DIR / "movie_review_bot.pkl"
VECTORIZER_PATH = MODELS_DIR / "vectorizer.pkl"

# Load model and vectorizer
model = joblib.load(MODEL_PATH)     
vectorizer = joblib.load(VECTORIZER_PATH)   

@app.route('/result', methods=["POST"])
def predict():
    data = request.get_json()
    review = data.get("review", "")
    vectorized_review = vectorizer.transform([review])
    prediction = model.predict(vectorized_review)
    probabilities = model.predict_proba(vectorized_review)
    confidence = round(probabilities[0][prediction[0]] * 100, 2)
    return jsonify({
        "prediction": int(prediction[0]),
        "confidence": confidence
    })

@app.route('/', methods=["GET"])
def default():
    return render_template("index.html")

@app.route("/health")
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")