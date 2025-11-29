import ollama
import os

class OllamaGenerate:

    def __init__(self):
        #self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))      
        #self.CSV_PATH = os.path.join(self.BASE_DIR, "..", "data", "cleaned_IMDB_Dataset.csv")
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.CSV_PATH = "/app/data/cleaned_IMDB_Dataset.csv"
        self.CSV_PATH = os.path.abspath(self.CSV_PATH)    
        self.prompt =  """
                        I need you to generate movie reviews, without using a movie name 
                        You must output EXACTLY 20 lines and NOTHING else.

                        CRITICAL FORMAT RULES:
                        1. Each line must contain exactly ONE review.
                        2. Each line must end with exactly one comma followed immediately by either:
                        positive
                        negative
                        3. You MUST place each review on its own line with NO blank lines.
                        4. The sentiment must be ONLY the word:
                        positive
                        negative
                        5. The sentiment must appear ONLY at the end of the line.
                        6. No numbers of any kind.
                        7. No extra commas or characters after the sentiment.
                        8. Each review must be between 35 and 155 words.

                        OUTPUT FORMAT EXAMPLE (copy this format EXACTLY, but with unique reviews):
                        some long review text goes here,positive
                        another review text goes here,negative

                        BEGIN NOW.
                        ...
                        """
        self.ai_output = ""

    def generateResponse(self):
        response = ollama.chat(model="gemma3:4b", messages=[{"role": "user", "content": self.prompt}])
        print("User:", self.prompt)
        print(response["message"]["content"])
        self.ai_output = response["message"]["content"]
        return self.ai_output
    
    def clean_response(self):
        if not self.ai_output:
            raise ValueError("No AI output found. Please call generateResponse() first.")

        import re

        self.cleaned_rows = []
        lines = self.ai_output.split("\n")

        for raw_line in lines:
            line = raw_line.strip()

            if not line:
                continue

            if "," not in line:
                print("Skipping malformed line (no comma):", line)
                continue

            review, sentiment = line.rsplit(",", 1)

            review = review.strip()
            sentiment = sentiment.strip().lower().rstrip("., ")

            # If sentiment is messy, extract keyword
            # Example: "deeply depressing" -> depressing
            sentiment = sentiment.split()[-1]  # keeps last word

            # Normalize synonyms
            positive_words = {"positive", "amazing", "heartwarming", "delightful", "charming", "moving", "thrilling", "impressive"}
            negative_words = {"negative", "depressing", "awful", "dreadful", "tiresome", "frustrating"}

            if sentiment in positive_words:
                sentiment = "positive"
            elif sentiment in negative_words:
                sentiment = "negative"
            else:
                print("Invalid sentiment, skipping:", sentiment)
                continue

            self.cleaned_rows.append([review, sentiment])

        return self.cleaned_rows

    def addData(self):
        if not hasattr(self, "cleaned_rows"):
            raise ValueError("No cleaned data found. Call clean_response() first.")

        with open(self.CSV_PATH, "a", encoding="utf-8") as file:
            for review, sentiment in self.cleaned_rows:
                file.write(f"{review},{sentiment}\n")

obj = OllamaGenerate()
obj.generateResponse()
obj.clean_response()
obj.addData()