import pandas as pd
import plotly.express as px

csv = pd.read_csv("assignment-data.csv")

graph = px.scatter(csv, x="date", y="cases",color="country")

graph.show()
