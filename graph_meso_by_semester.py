import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import DataFrame

def graph_meso_by_semester():

    total_arrivals_2011_a = total_arrivals_2011_b = total_arrivals_2011_c = total_arrivals_2011_d = 0
    total_arrivals_2012_a = total_arrivals_2012_b = total_arrivals_2012_c = total_arrivals_2012_d = 0
    total_arrivals_2013_a = total_arrivals_2013_b = total_arrivals_2013_c = total_arrivals_2013_d = 0
    total_arrivals_2014_a = total_arrivals_2014_b = total_arrivals_2014_c = total_arrivals_2014_d = 0
    total_arrivals_2015_a = total_arrivals_2015_b = total_arrivals_2015_c = total_arrivals_2015_d = 0

    df = pd.read_csv('xwra_2011_a_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2011_a = total_arrivals_2011_a + float(df.iloc[row, 3])

    df = pd.read_csv('xwra_2011_b_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2011_b = total_arrivals_2011_b + float(df.iloc[row, 3])

    total_arrivals_2011_b = total_arrivals_2011_b - total_arrivals_2011_a

    df = pd.read_csv('xwra_2011_c_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2011_c = total_arrivals_2011_c + float(df.iloc[row, 3])

    total_arrivals_2011_c = total_arrivals_2011_c - total_arrivals_2011_b - total_arrivals_2011_a

    df = pd.read_csv('xwra_2011_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2011_d = total_arrivals_2011_d + float(df.iloc[row, 3])

    total_arrivals_2011_d = total_arrivals_2011_d - total_arrivals_2011_c - total_arrivals_2011_b - total_arrivals_2011_a

    df = pd.read_csv('xwra_2012_a_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2012_a = total_arrivals_2012_a + float(df.iloc[row, 3])

    df = pd.read_csv('xwra_2012_b_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2012_b = total_arrivals_2012_b + float(df.iloc[row, 3])

    total_arrivals_2012_b = total_arrivals_2012_b - total_arrivals_2012_a

    df = pd.read_csv('xwra_2012_c_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2012_c = total_arrivals_2012_c + float(df.iloc[row, 3])

    total_arrivals_2012_c = total_arrivals_2012_c - total_arrivals_2012_b - total_arrivals_2012_a

    df = pd.read_csv('xwra_2012_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2012_d = total_arrivals_2012_d + float(df.iloc[row, 3])

    total_arrivals_2012_d = total_arrivals_2012_d - total_arrivals_2012_c - total_arrivals_2012_b - total_arrivals_2012_a

    df = pd.read_csv('xwra_2013_a_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2013_a = total_arrivals_2013_a + float(df.iloc[row, 3])

    df = pd.read_csv('xwra_2013_b_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2013_b = total_arrivals_2013_b + float(df.iloc[row, 3])

    total_arrivals_2013_b = total_arrivals_2013_b - total_arrivals_2013_a

    df = pd.read_csv('xwra_2013_c_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2013_c = total_arrivals_2013_c + float(df.iloc[row, 3])

    total_arrivals_2013_c = total_arrivals_2013_c - total_arrivals_2013_b - total_arrivals_2013_a

    df = pd.read_csv('xwra_2013_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2013_d = total_arrivals_2013_d + float(df.iloc[row, 3])

    total_arrivals_2013_d = total_arrivals_2013_d - total_arrivals_2013_c - total_arrivals_2013_b - total_arrivals_2013_a

    df = pd.read_csv('xwra_2014_a_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2014_a = total_arrivals_2014_a + float(df.iloc[row, 3])

    df = pd.read_csv('xwra_2014_b_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2014_b = total_arrivals_2014_b + float(df.iloc[row, 3])

    total_arrivals_2014_b = total_arrivals_2014_b - total_arrivals_2014_a

    df = pd.read_csv('xwra_2014_c_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2014_c = total_arrivals_2014_c + float(df.iloc[row, 3])

    total_arrivals_2014_c = total_arrivals_2014_c - total_arrivals_2014_b - total_arrivals_2014_a

    df = pd.read_csv('xwra_2014_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2014_d = total_arrivals_2014_d + float(df.iloc[row, 3])

    total_arrivals_2014_d = total_arrivals_2014_d - total_arrivals_2014_c - total_arrivals_2014_b - total_arrivals_2014_a

    df = pd.read_csv('xwra_2015_a_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2015_a = total_arrivals_2015_a + float(df.iloc[row, 3])

    df = pd.read_csv('xwra_2015_b_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2015_b = total_arrivals_2015_b + float(df.iloc[row, 3])

    total_arrivals_2015_b = total_arrivals_2015_b - total_arrivals_2015_a

    df = pd.read_csv('xwra_2015_c_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2015_c = total_arrivals_2015_c + float(df.iloc[row, 3])

    total_arrivals_2015_c = total_arrivals_2015_c - total_arrivals_2015_b - total_arrivals_2015_a

    df = pd.read_csv('xwra_2015_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_arrivals_2015_d = total_arrivals_2015_d + float(df.iloc[row, 3])

    total_arrivals_2015_d = total_arrivals_2015_d - total_arrivals_2015_c - total_arrivals_2015_b - total_arrivals_2015_a

    barWidth = 0.15

    # set height of bar
    bars_firstsem = [total_arrivals_2011_a, total_arrivals_2012_a, total_arrivals_2013_a, total_arrivals_2014_a,
                     total_arrivals_2015_a]
    bars_secondsem = [total_arrivals_2011_b, total_arrivals_2012_b, total_arrivals_2013_b, total_arrivals_2014_b,
                      total_arrivals_2015_b]
    bars_thirdsem = [total_arrivals_2011_c, total_arrivals_2012_c, total_arrivals_2013_c, total_arrivals_2014_c,
                     total_arrivals_2015_c]
    bars_fourthsem = [total_arrivals_2011_d, total_arrivals_2012_d, total_arrivals_2013_d, total_arrivals_2014_d,
                      total_arrivals_2015_d]

    # Set position of bar on X axis
    r_firstsem = np.arange(len(bars_firstsem))
    r_secondsem = [x + barWidth for x in r_firstsem]
    r_thirdsem = [x + barWidth for x in r_secondsem]
    r_fourthsem = [x + barWidth for x in r_thirdsem]

    # Make the plot
    plt.bar(r_firstsem, bars_firstsem, color='#7f6d5f', width=barWidth, edgecolor='white', label="First Semester")
    plt.bar(r_secondsem, bars_secondsem, color='#557f2d', width=barWidth, edgecolor='white', label="Second Semester")
    plt.bar(r_thirdsem, bars_thirdsem, color='#2d7f5e', width=barWidth, edgecolor='white', label="Third Semester")
    plt.bar(r_fourthsem, bars_fourthsem, color='#510f2f', width=barWidth, edgecolor='white', label="Fourth Semester")

    # Add xticks on the middle of the group bars
    plt.xlabel('Arrivals by Semester', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars_firstsem))], ["2011", "2012", "2013", "2014", "2015"])

    # Create legend & Show graphic
    plt.legend()
    plt.show()

    return bars_firstsem, bars_secondsem, bars_thirdsem, bars_fourthsem
