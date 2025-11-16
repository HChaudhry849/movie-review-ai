import pandas as pd
import matplotlib.pyplot as plt

def readData():
    df = pd.read_csv('IMDB_Dataset.csv')
    return df

def removeDuplicates(df):
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

def removeNull(df):
    # Remove rows with any NaN values
    df.dropna(inplace = True)

def toLowerCase(df):
    # Convert all string columns to lowercase
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.lower()

def removeSpecialChars(df):
    # Remove special characters from string columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)

def printData(x):
   print(df.columns)
   print(df.head())

def checkClassBalance(df):  
    # Check the balance of the 'sentiment' column
    print(df['sentiment'].value_counts())

def dropColumns(df, columns):
    # Drop specified columns from the DataFrame
    df.drop(columns=columns, inplace=True, errors='ignore')

def saveData(df):
    # Save the cleaned DataFrame to a new CSV file
    df.to_csv('cleaned_IMDB_Dataset.csv', index=False)

def checkColumns(df):
    res = df.columns
    print(res)

def plotData(df):
    # Create a new column 'review_length' counting words
    df['review_length'] = df['review'].apply(lambda x: len(str(x).split()))
    plt.hist(df['review_length'], bins=50)
    plt.title('Review Length Distribution')
    plt.xlabel('Number of Words')
    plt.ylabel('Number of Reviews')
    plt.savefig("output.png")  
    plt.close()  

df = readData()
removeDuplicates(df)        
removeNull(df)
toLowerCase(df)
removeSpecialChars(df)
printData(5)
checkClassBalance(df)
plotData(df)
dropColumns(df, ['id', 'review_length'])
checkColumns(df)
saveData(df)