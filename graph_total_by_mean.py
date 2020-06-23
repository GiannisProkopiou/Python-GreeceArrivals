import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import DataFrame

def graph_total_by_mean():

    total_plane_2011 = total_plane_2012 = total_plane_2013 = total_plane_2014 = total_plane_2015 = 0
    total_train_2011 = total_train_2012 = total_train_2013 = total_train_2014 = total_train_2015 = 0
    total_ship_2011 = total_ship_2012 = total_ship_2013 = total_ship_2014 = total_ship_2015 = 0
    total_car_2011 = total_car_2012 = total_car_2013 = total_car_2014 = total_car_2015 = 0

    df = pd.read_csv('meso_2011_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_plane_2011 = total_plane_2011 + float(df.iloc[row, 2])
        total_train_2011 = total_train_2011 + float(df.iloc[row, 3])
        total_ship_2011 = total_ship_2011 + float(df.iloc[row, 4])
        total_car_2011 = total_car_2011 + float(df.iloc[row, 5])

    df = pd.read_csv('meso_2012_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_plane_2012 = total_plane_2012 + float(df.iloc[row, 2])
        total_train_2012 = total_train_2012 + float(df.iloc[row, 3])
        total_ship_2012 = total_ship_2012 + float(df.iloc[row, 4])
        total_car_2012 = total_car_2012 + float(df.iloc[row, 5])

    df = pd.read_csv('meso_2013_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_plane_2013 = total_plane_2013 + float(df.iloc[row, 2])
        total_train_2013 = total_train_2013 + float(df.iloc[row,3])
        total_ship_2013 = total_ship_2013 + float(df.iloc[row, 4])
        total_car_2013 = total_car_2013 + float(df.iloc[row, 5])

    df = pd.read_csv('meso_2014_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_plane_2014 = total_plane_2014 + float(df.iloc[row, 2])
        total_train_2014 = total_train_2014 + float(df.iloc[row, 3])
        total_ship_2014 = total_ship_2014 + float(df.iloc[row, 4])
        total_car_2014 = total_car_2014 + float(df.iloc[row, 5])

    df = pd.read_csv('meso_2015_d_xl.csv', encoding='latin1')
    for row in range(len(df)):
        total_plane_2015 = total_plane_2015 + float(df.iloc[row, 2])
        total_train_2015 = total_train_2015 + float(df.iloc[row,3])
        total_ship_2015 = total_ship_2015 + float(df.iloc[row, 4])
        total_car_2015 = total_car_2015 + float(df.iloc[row, 5])

    # set width of bar
    barWidth = 0.15

    # set height of bar
    bars_plane = [total_plane_2011, total_plane_2012, total_plane_2013, total_plane_2014, total_plane_2015]
    bars_train = [total_train_2011, total_train_2012, total_train_2013, total_train_2014, total_train_2015]
    bars_ship = [total_ship_2011, total_ship_2012, total_ship_2013, total_ship_2014, total_ship_2015]
    bars_car = [total_car_2011, total_car_2012, total_car_2013, total_car_2014, total_car_2015]

    # Set position of bar on X axis
    r_plane = np.arange(len(bars_plane))
    r_train = [x + barWidth for x in r_plane]
    r_ship = [x + barWidth for x in r_train]
    r_car = [x + barWidth for x in r_ship]

    # Make the plot
    plt.bar(r_plane, bars_plane, color='#7f6d5f', width=barWidth, edgecolor='white', label="Plane")
    plt.bar(r_train, bars_train, color='#557f2d', width=barWidth, edgecolor='white', label="Train")
    plt.bar(r_ship, bars_ship, color='#2d7f5e', width=barWidth, edgecolor='white', label="Ship")
    plt.bar(r_car, bars_car, color='#510f2f', width=barWidth, edgecolor='white', label="Car")

    # Add xticks on the middle of the group bars
    plt.xlabel('Most Valuable Means of Transport', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars_plane))], ["2011", "2012", "2013", "2014", "2015"])

    # Create legend & Show graphic
    plt.legend()
    plt.show()

    return bars_plane,bars_train, bars_ship, bars_car