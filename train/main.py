from data import handle_data as hd
import vectorize_data as vd
import train_model as td
from evaluate import evaluation as ev
from dashboard import dashboard as db

class Main:

    def __init__(self):
        self.hData = hd.HandleData()
        self.vData = vd.VectorizeData(self.hData)
        self.tModel = td.TrainModel(self.vData)
        self.eVal = ev.Evaluation(self.tModel)
        self.db = db.Dashboard()

    def run(self):
        #data flow management (no duplicates) and ensure data is passed correctly 
        self.vData.get_data()
        self.vData.get_split_data()
        self.vData.allocate_data()
        self.vData.vectorize_review_data()
        self.vData.label_sentiment_data()
        self.tModel.get_training_data()
        self.tModel.feed_model()
        self.tModel.predict()
        self.tModel.seeResult()
        self.eVal.evaluate_model()
        self.eVal.load_file()
        self.eVal.save_file()

#this is what runs the overall code
if __name__ == "__main__":
   mainapp = Main()
   mainapp.run()
