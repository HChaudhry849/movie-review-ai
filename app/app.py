from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import joblib
app = Flask(__name__)
CORS(app)  # <-- Enable CORS

#Importing a library in one script doesn’t automatically share it with others.
#When you run app.py, it’s a new process.
#Think of imports like “bringing in tools” for that script’s work.
MODEL_PATH = "./models/movie_review_bot"
VECTORIZER_PATH = "./models/vectorizer.pkl"

model = joblib.load(MODEL_PATH)     
vectorizer = joblib.load(VECTORIZER_PATH)   

@app.route('/result', methods=["POST"])
def predict():
    #request the data
    data = request.get_json()
    #create key for json and dataformat e.g. string
    review = data.get("review", "")
    #call from loaded data - accessing from scikitlearn directly 
    vectorized_review = vectorizer.transform([review])
    #call from loaded data - accessing from scikitlearn directly 
    prediction = model.predict(vectorized_review)
    #tells us how much of the review belongs to positive vs negative
    probabilities = model.predict_proba(vectorized_review)
    # Pick the model’s guess and find out how sure it is about that guess
    # Takes the model’s own prediction and finds the matching confidence score (probability) for it
    confidence = round(probabilities[0][prediction[0]] * 100, 2)
    #always return the result, this returns array
    return jsonify({"prediction": int(prediction[0]),
                    "confidence": confidence})

@app.route('/', methods=["GET"])
def default():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)