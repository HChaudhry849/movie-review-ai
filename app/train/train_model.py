from sklearn.linear_model import LogisticRegression
import joblib
from pathlib import Path

class TrainModel:

    def __init__(self, vectorizer):
        self.training_dataX = None
        self.testing_dataX = None
        self.encoded_labelY = None
        self.encoded_test_labelY = None
        self.clf = None
        self.predictedLabel = None
        self.vd = vectorizer
        # project root
        self.root_dir = Path(__file__).resolve().parents[2]
        self.models_dir = self.root_dir / "models"
    
    def get_training_data(self):
        self.training_dataX, self.testing_dataX = self.vd.vectorize_review_data()
        self.encoded_labelY, self.encoded_test_labelY = self.vd.label_sentiment_data()
        return self.training_dataX, self.testing_dataX, self.encoded_labelY, self.encoded_test_labelY

    def feed_model(self):
        self.clf = LogisticRegression(random_state=0, max_iter=2000, solver='saga').fit(
            self.training_dataX, self.encoded_labelY
        )
        return self.clf
    
    def predict(self):
        self.predictedLabel = self.clf.predict(self.testing_dataX)
        return self.predictedLabel
    
    def seeResult(self):
        print(self.predictedLabel)

    def save_model(self):
        # Ensure models folder exists
        self.models_dir.mkdir(parents=True, exist_ok=True)
        
        clf_path = self.models_dir / "movie_review_bot.pkl"
        vect_path = self.models_dir / "vectorizer.pkl"

        joblib.dump(self.clf, clf_path)
        joblib.dump(self.vd.vectorizer, vect_path)

        print(f"Model saved to {clf_path}")
        print(f"Vectorizer saved to {vect_path}")
