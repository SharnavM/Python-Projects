import pandas as pd
import plotly.express as px
from covid import Covid
import openpyxl as opx

csv = pd.read_csv("covid_data.csv")

graph = px.scatter(csv, x="Country", y="Recovered",color="Country")

graph.show()
