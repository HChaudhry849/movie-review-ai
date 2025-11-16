from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

class Evaluation: 

    def __init__(self, trainer):
        self.td = trainer
        
    def check_accuracy(self):
        #pick specific variables
        encoded_test_labelY = self.td.encoded_test_labelY 
        predicted_answers = self.td.predictedLabel 
        accuracy = accuracy_score(encoded_test_labelY, predicted_answers)
        print(accuracy)

    def check_matrix(self):
        encoded_test_labelY = self.td.encoded_test_labelY 
        predicted_answers = self.td.predictedLabel 
        co_matrix = confusion_matrix(encoded_test_labelY, predicted_answers)
        print(co_matrix)

    def check_f1(self):
        encoded_test_labelY = self.td.encoded_test_labelY 
        predicted_answers = self.td.predictedLabel 
        f_score = f1_score(encoded_test_labelY, predicted_answers)
        print(f_score)

