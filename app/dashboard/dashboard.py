import streamlit as st
import pandas as pd
import json
import plotly.express as px
from pathlib import Path

class Dashboard:

    def buildChart(self):
        # Get project root dynamically (two levels above this file)
        root_dir = Path(__file__).resolve().parents[2]
        json_path = root_dir / "evaluate" / "history.json"

        if not json_path.exists():
            st.error(f"history.json not found at {json_path}")
            return

        # Load JSON
        with open(json_path, 'r') as file:
            data = json.load(file)

        # Convert metrics to DataFrame
        df = pd.DataFrame(data["metrics"])

        # Melt for plotting
        df_long = df.melt(
            id_vars="date",
            var_name="metric",
            value_name="score"
        )

        # Build bar chart
        figure = px.bar(
            df_long,
            x='date',
            y='score',
            color='metric',
            barmode='group',
            title='Evaluation Scores'
        )

        st.plotly_chart(figure)

if __name__ == "__main__":
    st.set_page_config(page_title="Evaluation Dashboard", layout="wide")
    st.title("Model Evaluation Dashboard")

    dashboard = Dashboard()
    dashboard.buildChart()