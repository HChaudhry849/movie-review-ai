import os
import csv
from pathlib import Path
import ollama  # Ensure Ollama is installed and importable

class OllamaGenerate:

    def __init__(self):
        # Root folder of the project (ML-E2E-FLOW)
        self.ROOT_DIR = Path(__file__).resolve().parents[0].parent  # This points to ML-E2E-FLOW
        self.CSV_PATH = self.ROOT_DIR / "data" / "cleaned_IMDB_Dataset.csv"

        # Prompt for AI-generated reviews
        self.prompt = """
        I need you to generate movie reviews, without using a movie name 
        You must output EXACTLY 20 lines and NOTHING else.

        CRITICAL FORMAT RULES:
        1. Each line must contain exactly ONE review.
        2. Each line must end with exactly one comma followed immediately by either:
           positive
           negative
        3. Each review must be between 35 and 155 words.
        OUTPUT FORMAT EXAMPLE:
        some long review text goes here,positive
        another review text goes here,negative
        """

        self.ai_output = ""

    def generate_response(self):
        """Generate AI movie reviews using Ollama"""
        response = ollama.chat(
            model="gemma3:4b",
            messages=[{"role": "user", "content": self.prompt}]
        )
        self.ai_output = response["message"]["content"]
        return self.ai_output

    def clean_response(self):
        """Parse AI output and normalize into [review, sentiment]"""
        if not self.ai_output:
            raise ValueError("No AI output found. Call generate_response() first.")

        self.cleaned_rows = []
        lines = self.ai_output.split("\n")

        for raw_line in lines:
            line = raw_line.strip()
            if not line or "," not in line:
                continue

            # Split only at the last comma
            review, sentiment = line.rsplit(",", 1)
            review = review.strip()
            sentiment = sentiment.strip().lower()

            # Normalize sentiment robustly
            if "positive" in sentiment:
                sentiment = "positive"
            elif "negative" in sentiment:
                sentiment = "negative"
            else:
                # Skip invalid sentiment
                continue

            self.cleaned_rows.append([review, sentiment])

        return self.cleaned_rows

    def add_data(self):
        """Append cleaned rows to the CSV safely"""
        if not hasattr(self, "cleaned_rows"):
            raise ValueError("No cleaned data found. Call clean_response() first.")

        os.makedirs(self.CSV_PATH.parent, exist_ok=True)

        with open(self.CSV_PATH, "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            for review, sentiment in self.cleaned_rows:
                writer.writerow([review, sentiment])


obj = OllamaGenerate()
obj.generate_response()  # correct method name
obj.clean_response()
obj.add_data()     