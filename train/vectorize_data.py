from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class VectorizeData:
    """Class to handle data vectorization and preparation for sentiment analysis."""
    def __init__(self, hd_instance):
        self.data = None
        self.X_train = None
        self.X_test = None  
        self.y_train = None
        self.y_test = None
        self.X = None
        self.y = None
        self.X_train_vectorized = None
        self.X_test_vectorized = None
        self.y_train_label = None
        self.y_train_encoded = None
        self.y_test_encoded = None
        #pass the entire object of HandleData
        self.hd = hd_instance

    def get_data(self):
        self.data = self.hd.load_data()
        return self.data

    def get_split_data(self):  
        # Split the dataset into features and target variable
        self.X, self.y = self.hd.split_data(self.data)
        return self.X, self.y

    def allocate_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.25, random_state=42)
        return self.X_train, self.X_test, self.y_train, self.y_test

    def vectorize_review_data(self):
        # Create a CountVectorizer instance
        self.vectorizer = CountVectorizer(max_features=10000)
        # Fit the vectorizer on the training data and transform both train and test data
        self.X_train_vectorized = self.vectorizer.fit_transform(self.X_train)
        self.X_test_vectorized = self.vectorizer.transform(self.X_test)
        return self.X_train_vectorized, self.X_test_vectorized

    def label_sentiment_data(self):
        le = LabelEncoder()
        # first fit transform on the training labels, this means learn the mapping e.g. 'positive' -> 1, 'negative' -> 0
        # and convwert the training labels to numbers
        self.y_train_encoded = le.fit_transform(self.y_train)
        # Now transform the test labels using the same mapping learned from the training labels 
        # but do not learn again
        self.y_test_encoded = le.transform(self.y_test)
        return self.y_train_encoded, self.y_test_encoded
    
    
    