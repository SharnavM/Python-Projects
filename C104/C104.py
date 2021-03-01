import csv

#Avg - 68.13352
#Med - 68.2166

with open("Custom.csv", newline="") as f:
    file = csv.reader(f)
    s = list(file)

s.pop(0)

def Mean(arr):
    avg_ht_arr = [float(i[1])/len(arr) for i in arr]

    avg_ht = 0
    for i in avg_ht_arr:
        avg_ht += i
    print("Mean of all heights is {}".format(avg_ht))

def Median(arr):
    if len(arr)%2 == 0:
        median1_ht = arr[int((len(arr)/2) + 1)][1]
        median2_ht = arr[int(len(arr)/2)][1]
        median_ht = (float(median1_ht)+  float(median2_ht))/2
    else:
       val = arr[int((len(arr)+1)/2)][1]
       median_ht = float(val)
    print("Median Height is {}".format(median_ht))

def Mode(arr):
    mode_arr = []
    for i in arr:
        mode_arr.append(round(float(i[1]),2))
    print("Mode of Height is ", max(list(set(mode_arr)), key=list(mode_arr).count))     

Mean(s)
Median(s)
Mode(s)
