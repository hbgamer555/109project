import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics

df=pd.read_csv(r"C:\Users\ADMIN\New folder (3)\StudentsPerformance.csv")
data=df["math score"].tolist()
#print(data)
mean1=statistics.mean(data)
print(mean1)
median1=statistics.median(data)
print(median1)
mode1=statistics.mode(data)
print(mode1)

st_dv1=statistics.stdev(data)
print(st_dv1)
first_stdev_start,first_stdev_end=mean1-(1*st_dv1),mean1+(1*st_dv1)
second_stdev_start,second_stdev_end=mean1-(2*st_dv1),mean1+(2*st_dv1)
third_stdev_start,third_stdev_end=mean1=(3*st_dv1),mean1+(3*st_dv1)

first_stdev_value=[value for value in data if value > first_stdev_start and value < first_stdev_end]
second_stdev_value=[value for value in data if value > second_stdev_start and value < second_stdev_end]
third_stdev_value=[value for value in data if value > third_stdev_start and value < third_stdev_end]

first_percentage =len(first_stdev_value)*100/len(data)
print(first_percentage)
second_percentage =len(second_stdev_value)*100/len(data)
print(second_percentage)
third_percentage =len(third_stdev_value)*100/len(data)
print(third_percentage)