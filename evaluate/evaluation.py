from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

class Evaluation: 
   
    def __init__(self, trainer):
        self.td = trainer

    def evaluate_model(self):
        THRESHOLDS = {
            "accuracy": 0.85, 
            "f1": 0.80
        }

        encoded_test_labelY = self.td.encoded_test_labelY 
        predicted_answers = self.td.predictedLabel 

        accuracy = accuracy_score(encoded_test_labelY, predicted_answers)
        print(accuracy)

        f_score = f1_score(encoded_test_labelY, predicted_answers)
        print(f_score)

        co_matrix = confusion_matrix(encoded_test_labelY, predicted_answers)
        print(co_matrix)

        if accuracy >= THRESHOLDS["accuracy"] and f_score >= THRESHOLDS["f1"]:
            self.td.save_model()
            print("Model passed evaluation - saved")
        else:
            print("Model failed evaluation - NOT saved")