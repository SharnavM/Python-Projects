import plotly.express as px

data= [60,61,65,63,98,99,90,95,91,96]

def Mean(arr):
    avg_arr = [int(i)/len(arr) for i in arr]

    avg = 0
    for i in avg_arr:
        avg += i
    print("Average  of given data is {0:.2f}".format(avg))
    return avg

def calc_deviation(arr, mean):
    arr = [int(i) for i in arr]
    add = 0
    for i in arr:
        add += (i-mean)**2
    frac = add/(len(arr)-1)
    dev = frac**0.5
    return dev

mean = Mean(data)
deviation = calc_deviation(data, mean)

graph = px.scatter(data, title="Deviation is {0:.2f}".format(deviation))
graph.add_shape(dict(type="line", x0=0, x1=len(data), y0=mean, y1=mean))
graph.update_layout(showlegend=False)
graph.show()
