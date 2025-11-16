import pandas as pd
import matplotlib.pyplot as plt

class CleanData:

    def __init__(self):
        self.df = None
        self.cleaned_set = None
    
    def load_data(self):
        self.df = pd.read_csv('sentiment_analysis.csv')
        self.cleaned_set = self.df.copy()
        return self.cleaned_set

#basic inspection to check first 10 rows 
    def inspect_data(self):
        self.first_10_rows = self.cleaned_set.head(10)
    
#removes various undeed columns
    def remove_columns(self):
       self.cleaned_set = self.cleaned_set.drop(['Time of Tweet', 'Platform'], axis='columns')
       return self.cleaned_set

#counts total words in the text column
    def number_of_words(self):
        self.cleaned_set['text_word_count'] = self.cleaned_set['text'].str.split().str.len()
        return self.cleaned_set

#class distribution to check data size for sentiment positive vs negative
    def class_distribution(self): 
        print(self.cleaned_set.groupby("sentiment").size())

#removes all duplicate rows
    def remove_duplicates(self):
        self.cleaned_set = self.cleaned_set.drop_duplicates()
        return self.cleaned_set
    
#changes data to lowercase
    def lower_case(self):
        for col in self.cleaned_set.select_dtypes(include=['object']).columns:
            self.cleaned_set[col] = self.cleaned_set[col].str.lower()
        return self.cleaned_set
    
#removes spceial characters from the data
    def remove_special_char(self):
        for col in self.cleaned_set.select_dtypes(include=['object']).columns:
            #replace anything that is not r'[^a-zA-Z0-9 ]
            self.cleaned_set[col] = self.cleaned_set[col].str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
        return self.cleaned_set

#removes null values
    def remove_null(self):
        self.cleaned_set['text_imputed'] = self.cleaned_set['text'].isna()
        return self.cleaned_set

    def bar_chart(self):
        plt.figure(figsize=(10, 8))
        #counts the values in sentiment column 
        self.cleaned_set['sentiment'].value_counts().plot.bar()
        plt.title("Sentiment Distribution")
        plt.xlabel("Sentiment")
        plt.ylabel("Number of Texts")        
        plt.savefig("output.png")  
    
    def line_chart(self):
        plt.figure(figsize=(10, 8))
        self.cleaned_set['sentiment'].value_counts().plot.line()
        plt.title("Sentiment Distribution")
        plt.xlabel("Sentiment")
        plt.ylabel("Number of Texts")        
        plt.savefig("output_line.png") 
    
    def histogram(self):
        plt.figure(figsize=(10, 8))
        self.cleaned_set['text_word_count'] = self.cleaned_set['text'].str.split().str.len()
        plt.hist(self.cleaned_set['text_word_count'])               
        plt.savefig("output_histogram.png") 
        
    def save_csv(self):
        self.cleaned_set.to_csv('cleaned_data.csv', index=False)
    
cl = CleanData()
#Try block for checking file
try:
    #loading data to manipulate, try cannot be placed on def, use try when calling function
        cl.load_data()
except: 
        print("File does not exist!")

cl.inspect_data()
cl.remove_columns()
cl.number_of_words()
cl.class_distribution()
cl.remove_duplicates()
cl.lower_case()
cl.remove_special_char()
cl.remove_null()
cl.bar_chart()
cl.line_chart()
cl.histogram()
cl.save_csv()
