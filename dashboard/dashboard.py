import streamlit as st
import pandas as pd
import json 
import plotly.express as px


class Dashboard:

    def buildChart():
        with open('evaluate/history.json', 'r') as file:
            data = json.load(file)

        df = pd.DataFrame(data["metrics"])

        df_long = df.melt(
            id_vars="date",
            var_name="metric",
            value_name="score"
        )

        figure = px.bar(
            df_long,
            x='date',
            y='score',
            color='metric',
            barmode='group',
            title='Evaluation Scores'
        )

        st.plotly_chart(figure)