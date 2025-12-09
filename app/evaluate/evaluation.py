from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from datetime import date
import json
from pathlib import Path

class Evaluation: 
   
    def __init__(self, trainer):
        self.td = trainer
        # Path to project root / evaluate / history.json
        self.file_path = Path(__file__).resolve().parents[2] / "evaluate" / "history.json"
        self.contents = []

    def evaluate_model(self):
        THRESHOLDS = {
            "accuracy": 0.85, 
            "f1": 0.80
        }

        encoded_test_labelY = self.td.encoded_test_labelY 
        predicted_answers = self.td.predictedLabel 

        self.accuracy = accuracy_score(encoded_test_labelY, predicted_answers)
        print(self.accuracy)

        self.f_score = f1_score(encoded_test_labelY, predicted_answers)
        print(self.f_score)

        co_matrix = confusion_matrix(encoded_test_labelY, predicted_answers)
        print(co_matrix)

        if self.accuracy >= THRESHOLDS["accuracy"] and self.f_score >= THRESHOLDS["f1"]:
            self.td.save_model()
            print("Model passed evaluation - saved")
        else:
            print("Model failed evaluation - NOT saved")
        
        return self.accuracy, self.f_score

    def load_file(self):
        try:
            with open(self.file_path, "r") as f:
                self.contents = json.load(f)
        except FileNotFoundError:
            print(f"File not found at {self.file_path}, creating new file")
            self.contents = {"metrics": []}
        return self.contents

    def save_file(self):
        data = self.load_file()
        today = str(date.today())

        new_record = {
            "date": today,
            "accuracy": self.accuracy,
            "f1_score": self.f_score
        }

        data["metrics"].append(new_record)

        # Ensure parent folder exists
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
