import pandas as pd

class HandleData:
    
    def __init__(self):
        self.data = None
        self.X = None
        self.y = None

    def load_data(self):
        # Load the dataset from a CSV file
        self.data = pd.read_csv('cleaned_IMDB_Dataset.csv')
        return self.data

    def split_data(self, data):  
        # Split the dataset into features and target variable
        self.X = data['review']
        self.y = data['sentiment']
        return self.X, self.y