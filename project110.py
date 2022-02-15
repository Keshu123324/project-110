import random as rand
import plotly.figure_factory as ff
import statistics as s
import plotly.graph_objects as go
import pandas as pd

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

#calculating mean and standard deviation
population_mean=s.mean(data)
print("The population_mean is: ", population_mean)
std_deviation=s.stdev(data)
print("The standard deviation is: ",std_deviation)

#function to get the mean of the given data samples
def random_set_of_mean(counter):
    data_set=[]
    for i in range(0,counter):
        index=rand.randint(0,len(data)-1)
        value=data[index]
        data_set.append(value)

    mean=s.mean(data_set)
    return mean

#function to plot mean on the graph
def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

#function to get the mean of 30 data points 100 and plot the graph
def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()