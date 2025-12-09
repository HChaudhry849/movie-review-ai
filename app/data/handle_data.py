import pandas as pd
from pathlib import Path

class HandleData:

    def __init__(self):
        self.X = None
        self.y = None
        self.data_path = Path(__file__).resolve().parents[2] / "data" / "cleaned_IMDB_Dataset.csv"

    def load_data(self):
        """
        Load CSV robustly, handling:
        - Extra commas inside reviews
        - Proper quoting
        - Ensuring only two columns: review, sentiment
        """
        # Use quoting and error_bad_lines / on_bad_lines
        try:
            data = pd.read_csv(
                self.data_path,
                quotechar='"',  # Respect quoted fields
                engine="python",  # Python engine is more forgiving
                on_bad_lines='skip'  # Skip malformed lines
            )
        except Exception as e:
            raise RuntimeError(f"Failed to load CSV: {e}")

        # Ensure only 'review' and 'sentiment' columns
        if list(data.columns) != ["review", "sentiment"]:
            # Sometimes extra unnamed columns appear due to bad commas
            data = data.iloc[:, :2]
            data.columns = ["review", "sentiment"]

        # Clean sentiment column
        data["sentiment"] = data["sentiment"].str.lower().str.strip()
        data = data[data["sentiment"].isin({"positive", "negative"})]

        return data

    def split_data(self, data):
        self.X = data["review"]
        self.y = data["sentiment"]
        return self.X, self.y
