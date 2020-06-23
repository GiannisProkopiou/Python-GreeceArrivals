import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import DataFrame

def graph_total_arrivals_by_year():

    total_arrivals_2011 = total_arrivals_2012 = total_arrivals_2013 = total_arrivals_2014 = total_arrivals_2015 = 0

    df = pd.read_csv('D:\Python_Project_Compilers/xwra_2011_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2011 = total_arrivals_2011 + float(df.iloc[row, 3])

    df = pd.read_csv('xwra_2012_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2012 = total_arrivals_2012 + float(df.iloc[row, 3])

    df = pd.read_csv('xwra_2013_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2013 = total_arrivals_2013 + float(df.iloc[row, 3])

    df = pd.read_csv('xwra_2014_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2014 = total_arrivals_2014 + float(df.iloc[row, 3])

    df = pd.read_csv('xwra_2015_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2015 = total_arrivals_2015 + float(df.iloc[row, 3])

    # data
    df_total_arrivals_by_year = pd.DataFrame({'x': ("2011", "2012", "2013", "2014", "2015"), 'y': (
        total_arrivals_2011, total_arrivals_2012, total_arrivals_2013, total_arrivals_2014, total_arrivals_2015)})

    # plot
    plt.plot('x', "y", data=df_total_arrivals_by_year, linestyle='-', marker='o')
    plt.show()

    return df_total_arrivals_by_year