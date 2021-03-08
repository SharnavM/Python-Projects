import pandas as pd
import plotly.express as px
import csv
import numpy as np

csv1 = pd.read_csv("data1.csv")
csv2 = pd.read_csv("data2.csv")
csv3 = pd.read_csv("data3.csv")

x1= [i[0] for i in csv1.values.tolist()]
y1 = [i[1] for i in csv1.values.tolist()]

x2= [i[1] for i in csv2.values.tolist()]
y2 = [i[2] for i in csv2.values.tolist()]

x3= [i[0] for i in csv3.values.tolist()]
y3 = [i[1] for i in csv3.values.tolist()]

corr1 = np.corrcoef(x1, y1)[0,1]
corr2 = np.corrcoef(x2, y2)[0,1]
corr3 = np.corrcoef(x3, y3)[0,1]


'''graph1 = px.scatter(csv1, x="Temperature", y="Ice-cream Sales")
graph1.show()

graph2 = px.scatter(csv2, x="Coffee in ml", y="sleep in hours")
graph2.show()'''
