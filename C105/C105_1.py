import csv as cv
import plotly.express as px
import pandas as pd

csv = pd.read_csv("class1.csv")

with open("class1.csv", newline="") as f:
    s = cv.reader(f)
    s = list(s)
    
s.pop(0)
#dev = 21.255

def Mean(arr):
    avg_m_arr = [int(i[1])/len(arr) for i in arr]

    avg_mark = 0
    for i in avg_m_arr:
        avg_mark += i
    print("Average Marks of All students is {0:.2f}".format(avg_mark))
    return avg_mark

def calc_deviation(arr, mean):
    arr = [int(i[1]) for i in arr]
    add = 0
    for i in arr:
        add += (i-mean)**2
    frac = add/(len(arr)-1)
    dev = frac**0.5
    return dev

mean = Mean(s)
dev = calc_deviation(s, mean)

print("Deviation is ",dev)

graph = px.scatter(csv, x="Student Number", y="Marks",color="Student Number")

graph.add_shape(dict(type="line", x0=0, x1=30, y0=mean, y1=mean))
graph.update_layout(yaxis_range=[0,100])
graph.show()
