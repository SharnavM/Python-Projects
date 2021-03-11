import pandas as pd
import csv
import numpy as np

csv1 = pd.read_csv("assignment.csv")

x= [i[0] for i in csv1.values.tolist()]
y = [i[1] for i in csv1.values.tolist()]


corr = np.corrcoef(x, y)[0,1]

print(corr)
