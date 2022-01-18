import csv
import numpy as np

def getDataSource(data_path):
    tv = []
    average = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tv.append(float(row["Size of TV"]))
            average.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return {"x":tv,"y":average}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print(correlation[0,1])

def setup():
    data_path = "tv.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()