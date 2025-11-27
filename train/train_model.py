from sklearn.linear_model import LogisticRegression
import joblib
import os

class TrainModel:

    def __init__(self, vectorizer):
        self.training_dataX = None
        self.testing_dataX = None
        self.encoded_labelY = None
        self.encoded_test_labelY = None
        self.clf = None
        self.predictedLabel = None
        self.vd = vectorizer
        
    def get_training_data(self):
        self.training_dataX, self.testing_dataX = self.vd.vectorize_review_data()
        self.encoded_labelY, self.encoded_test_labelY = self.vd.label_sentiment_data()
        return self.training_dataX, self.testing_dataX, self.encoded_labelY, self.encoded_test_labelY

    def feed_model(self):
        self.clf = LogisticRegression(random_state=0,max_iter=2000,solver='saga').fit(self.training_dataX, self.encoded_labelY)
        return self.clf
    
    def predict(self):
        #returns the predicted value 
        self.predictedLabel = self.clf.predict(self.testing_dataX)
        return self.predictedLabel
    
    def seeResult(self):
        print(self.predictedLabel)

    def save_model(self):
        os.makedirs("models", exist_ok=True)
        joblib.dump(self.clf, "models/movie_review_bot.pkl")
        joblib.dump(self.vd.vectorizer, "models/vectorizer.pkl")
