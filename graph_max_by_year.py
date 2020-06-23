import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import DataFrame

def graph_max_by_year():

    max_2011 = max_2012 = max_2013 = max_2014 = max_2015 = 0

    df = pd.read_csv('D:\Python_Project_Compilers/xwra_2011_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        if max_2011 < float(df.iloc[row, 3]):
            max_2011 = float(df.iloc[row, 3])
            nation_max_2011 = df.iloc[row, 1]

    df = pd.read_csv('xwra_2012_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        if max_2012 < float(df.iloc[row, 3]):
            max_2012 = float(df.iloc[row, 3])
            nation_max_2012 = df.iloc[row, 1]

    df = pd.read_csv('xwra_2013_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        if max_2013 < float(df.iloc[row, 3]):
            max_2013 = float(df.iloc[row, 3])
            nation_max_2013 = df.iloc[row, 1]

    df = pd.read_csv('xwra_2014_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        if max_2014 < float(df.iloc[row, 3]):
            max_2014 = float(df.iloc[row, 3])
            nation_max_2014 = df.iloc[row, 1]

    df = pd.read_csv('xwra_2015_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        if max_2015 < float(df.iloc[row, 3]):
            max_2015 = float(df.iloc[row, 3])
            nation_max_2015 = df.iloc[row, 1]

    # set width of bar
    barWidth = 0.25

    # set height of bar
    bars_max = [max_2011, max_2012, max_2013, max_2014, max_2015]

    # Set position of bar on X axis
    r1 = np.arange(len(bars_max))

    # Make the plot
    plt.bar(r1, bars_max, color='#7f6d5f', width=barWidth, edgecolor='white')  # label=nation_max_2011)

    # Add xticks on the middle of the group bars
    plt.xlabel('Most Valuable Nations', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars_max))],
               ["2011: \n" + str(nation_max_2011), "2012: \n" + str(nation_max_2012),
                "2013: \n" + str(nation_max_2013),
                "2014: \n" + str(nation_max_2014), "2015: \n" + str(nation_max_2015)])

    # Create legend & Show graphic
    plt.legend()
    plt.show()

    return bars_max