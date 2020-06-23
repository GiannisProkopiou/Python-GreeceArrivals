import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import DataFrame

def graph_data_from_db():

    total_arrivals_2011_a = total_arrivals_2011_b = total_arrivals_2011_c = total_arrivals_2011_d = 0
    total_arrivals_2012_a = total_arrivals_2012_b = total_arrivals_2012_c = total_arrivals_2012_d = 0
    total_arrivals_2013_a = total_arrivals_2013_b = total_arrivals_2013_c = total_arrivals_2013_d = 0
    total_arrivals_2014_a = total_arrivals_2014_b = total_arrivals_2014_c = total_arrivals_2014_d = 0
    total_arrivals_2015_a = total_arrivals_2015_b = total_arrivals_2015_c = total_arrivals_2015_d = 0
    max_2011 = max_2012 = max_2013 = max_2014 = max_2015 = 0
    total_plane_2011 = total_plane_2012 = total_plane_2013 = total_plane_2014 = total_plane_2015 = 0
    total_train_2011 = total_train_2012 = total_train_2013 = total_train_2014 = total_train_2015 = 0
    total_ship_2011 = total_ship_2012 = total_ship_2013 = total_ship_2014 = total_ship_2015 =0
    total_car_2011 = total_car_2012 = total_car_2013 = total_car_2014 = total_car_2015 =0
    total_arrivals_2011 = total_arrivals_2012 = total_arrivals_2013 = total_arrivals_2014 = total_arrivals_2015 = 0
    nation_bars = []
    with open('xwra_2011_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2011 = total_arrivals_2011 + float(row["year_now"])
            nation_bars.append(row["nation"])

            if max_2011 < float(row["year_now"]):
                max_2011 = float(row["year_now"])
                nation_max_2011 = row["nation"]

    with open('xwra_2012_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2012 = total_arrivals_2012 + float(row["year_now"])

            if max_2012 < float(row["year_now"]):
                max_2012 = float(row["year_now"])
                nation_max_2012 = row["nation"]

    with open('xwra_2013_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2013 = total_arrivals_2013 + float(row["year_now"])

            if max_2013 < float(row["year_now"]):
                max_2013 = float(row["year_now"])
                nation_max_2013 = row["nation"]

    with open('xwra_2014_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            total_arrivals_2014 = total_arrivals_2014 + float(row["year_now"])

            if max_2014 < float(row["year_now"]):
                max_2014 = float(row["year_now"])
                nation_max_2014 = row["nation"]

    with open('xwra_2015_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2015 = total_arrivals_2015 + float(row["year_now"])

            if max_2015 < float(row["year_now"]):
                max_2015 = float(row["year_now"])
                nation_max_2015 = row["nation"]

    #------------------------------------

    with open('meso_2011_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_plane_2011 = total_plane_2011 + float(row["plane"])
            #total_train_2011 = total_train_2011 + float(row["train"])
            total_ship_2011 = total_ship_2011 + float(row["ship"])
            total_car_2011 = total_car_2011 + float(row["car"])

    with open('meso_2012_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_plane_2012 = total_plane_2012 + float(row["plane"])
            total_train_2012 = total_train_2012 + float(row["train"])
            total_ship_2012 = total_ship_2012 + float(row["ship"])
            total_car_2012 = total_car_2012 + float(row["car"])

    with open('meso_2013_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_plane_2013 = total_plane_2013 + float(row["plane"])
            #total_train_2013 = total_train_2013 + float(row["train"])
            total_ship_2013 = total_ship_2013 + float(row["ship"])
            total_car_2013 = total_car_2013 + float(row["car"])

    with open('meso_2014_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_plane_2014 = total_plane_2014 + float(row["plane"])
            total_train_2014 = total_train_2014 + float(row["train"])
            total_ship_2014 = total_ship_2014 + float(row["ship"])
            total_car_2014 = total_car_2014 + float(row["car"])

    with open('meso_2015_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_plane_2015 = total_plane_2015 + float(row["plane"])
            #total_train_2015 = total_train_2015 + float(row["train"])
            total_ship_2015 = total_ship_2015 + float(row["ship"])
            total_car_2015 = total_car_2015 + float(row["car"])

    #----------------------------------

    with open('xwra_2011_a.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2011_a = total_arrivals_2011_a + float(row["year_now"])


    with open('xwra_2011_b.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2011_b = total_arrivals_2011_b + float(row["year_now"])

        total_arrivals_2011_b = total_arrivals_2011_b - total_arrivals_2011_a

    with open('xwra_2011_c.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2011_c = total_arrivals_2011_c + float(row["year_now"])

        total_arrivals_2011_c = total_arrivals_2011_c - total_arrivals_2011_b - total_arrivals_2011_a

    with open('xwra_2011_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            total_arrivals_2011_d = total_arrivals_2011_d + float(row["year_now"])

        total_arrivals_2011_d = total_arrivals_2011_d - total_arrivals_2011_c - total_arrivals_2011_b - total_arrivals_2011_a

    with open('xwra_2012_a.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2012_a = total_arrivals_2012_a + float(row["year_now"])


    with open('xwra_2012_b.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2012_b = total_arrivals_2012_b + float(row["year_now"])

        total_arrivals_2012_b = total_arrivals_2012_b - total_arrivals_2012_a

    with open('xwra_2012_c.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2012_c = total_arrivals_2012_c + float(row["year_now"])

        total_arrivals_2012_c = total_arrivals_2012_c - total_arrivals_2012_b - total_arrivals_2012_a

    with open('xwra_2012_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            total_arrivals_2012_d = total_arrivals_2012_d + float(row["year_now"])

        total_arrivals_2012_d = total_arrivals_2012_d - total_arrivals_2012_c - total_arrivals_2012_b - total_arrivals_2012_a

    with open('xwra_2013_a.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2013_a = total_arrivals_2013_a + float(row["year_now"])


    with open('xwra_2013_b.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2013_b = total_arrivals_2013_b + float(row["year_now"])

        total_arrivals_2013_b = total_arrivals_2013_b - total_arrivals_2013_a

    with open('xwra_2013_c.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2013_c = total_arrivals_2013_c + float(row["year_now"])

        total_arrivals_2013_c = total_arrivals_2013_c - total_arrivals_2013_b - total_arrivals_2013_a

    with open('xwra_2013_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            total_arrivals_2013_d = total_arrivals_2013_d + float(row["year_now"])

        total_arrivals_2013_d = total_arrivals_2013_d - total_arrivals_2013_c - total_arrivals_2013_b - total_arrivals_2013_a

    with open('xwra_2014_a.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2014_a = total_arrivals_2014_a + float(row["year_now"])


    with open('xwra_2014_b.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2014_b = total_arrivals_2014_b + float(row["year_now"])

        total_arrivals_2014_b = total_arrivals_2014_b - total_arrivals_2014_a

    with open('xwra_2014_c.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2014_c = total_arrivals_2014_c + float(row["year_now"])

        total_arrivals_2014_c = total_arrivals_2014_c - total_arrivals_2014_b - total_arrivals_2014_a

    with open('xwra_2014_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            total_arrivals_2014_d = total_arrivals_2014_d + float(row["year_now"])

        total_arrivals_2014_d = total_arrivals_2014_d - total_arrivals_2014_c - total_arrivals_2014_b - total_arrivals_2014_a

    with open('xwra_2015_a.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2015_a = total_arrivals_2015_a + float(row["year_now"])


    with open('xwra_2012_b.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2015_b = total_arrivals_2015_b + float(row["year_now"])

        total_arrivals_2015_b = total_arrivals_2015_b - total_arrivals_2015_a

    with open('xwra_2012_c.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            total_arrivals_2015_c = total_arrivals_2015_c + float(row["year_now"])

        total_arrivals_2015_c = total_arrivals_2015_c - total_arrivals_2015_b - total_arrivals_2015_a

    with open('xwra_2015_d.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            total_arrivals_2015_d = total_arrivals_2015_d + float(row["year_now"])

        total_arrivals_2015_d = total_arrivals_2015_d - total_arrivals_2015_c - total_arrivals_2015_b - total_arrivals_2015_a

    print(total_arrivals_2011_a)
    print(total_arrivals_2011_b)
    print(total_arrivals_2011_c)
    print(total_arrivals_2011_d)

    print(total_arrivals_2012_a)
    print(total_arrivals_2012_b)
    print(total_arrivals_2012_c)
    print(total_arrivals_2012_d)

    print(total_arrivals_2013_a)
    print(total_arrivals_2013_b)
    print(total_arrivals_2013_c)
    print(total_arrivals_2013_d)

    print(total_arrivals_2014_a)
    print(total_arrivals_2014_b)
    print(total_arrivals_2014_c)
    print(total_arrivals_2014_d)

    print(total_arrivals_2015_a)
    print(total_arrivals_2015_b)
    print(total_arrivals_2015_c)
    print(total_arrivals_2015_d)



    # data
    df = pd.DataFrame({'x': ("2011", "2012", "2013", "2014", "2015"), 'y': (total_arrivals_2011, total_arrivals_2012 ,total_arrivals_2013, total_arrivals_2014,total_arrivals_2015 )})

    # plot
    plt.plot('x', "y", data=df, linestyle='-', marker='o')
    plt.show()

    #---------------------------------------

    # set width of bar
    barWidth = 0.25

    # set height of bar
    bars1 = [max_2011, max_2012, max_2013, max_2014, max_2015]

    # Set position of bar on X axis
    r1 = np.arange(len(bars1))

    # Make the plot
    plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white') #label=nation_max_2011)

    # Add xticks on the middle of the group bars
    plt.xlabel('Most Valuable Nations', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], [ "2011: \n" + nation_max_2011, "2012: \n" + nation_max_2012, "2013: \n" + nation_max_2013, "2014: \n" +nation_max_2014, "2015: \n" +nation_max_2015 ])

    # Create legend & Show graphic
    plt.legend()
    plt.show()


    # set width of bar
    barWidth = 0.25

    #---------------------------------------------

    # set height of bar
    bars_plane = [total_plane_2011, total_plane_2012, total_plane_2013, total_plane_2014, total_plane_2015]
    bars_train = [total_train_2011, total_train_2012, total_train_2013, total_train_2014, total_train_2015]
    bars_ship = [total_ship_2011, total_ship_2012, total_ship_2013, total_ship_2014, total_ship_2015]
    bars_car  = [total_car_2011, total_car_2012, total_car_2013, total_car_2014, total_car_2015]

    # Set position of bar on X axis
    r_plane = np.arange(len(bars_plane))
    r_train = [x + barWidth for x in r_plane]
    r_ship = [x + barWidth for x in r_train]
    r_car = [x + barWidth for x in r_ship]


    # Make the plot
    plt.bar(r_plane, bars_plane, color='#7f6d5f', width=barWidth, edgecolor='white',label="Plane")
    plt.bar(r_train, bars_train, color='#557f2d', width=barWidth, edgecolor='white', label="Train")
    plt.bar(r_ship, bars_ship, color='#2d7f5e', width=barWidth, edgecolor='white', label="Ship")
    plt.bar(r_car, bars_car, color='#510f2f', width=barWidth, edgecolor='white', label="Car")



    # Add xticks on the middle of the group bars
    plt.xlabel('Most Valuable Means of Transport', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], [ "2011", "2012", "2013" , "2014" , "2015"])

    # Create legend & Show graphic
    plt.legend()
    plt.show()

    #--------------------

    # set height of bar
    bars_firstsem = [total_arrivals_2011_a, total_arrivals_2012_a, total_arrivals_2013_a, total_arrivals_2014_a, total_arrivals_2015_a]
    bars_secondsem = [total_arrivals_2011_b, total_arrivals_2012_b, total_arrivals_2013_b, total_arrivals_2014_b, total_arrivals_2015_b]
    bars_thirdsem = [total_arrivals_2011_c ,  total_arrivals_2012_c, total_arrivals_2013_c, total_arrivals_2014_c, total_arrivals_2015_c]
    bars_fourthsem  = [total_arrivals_2011_d, total_arrivals_2012_d, total_arrivals_2013_d, total_arrivals_2014_d, total_arrivals_2015_d]

    # Set position of bar on X axis
    r_firstsem = np.arange(len(bars_firstsem))
    r_secondsem = [x + barWidth for x in r_plane]
    r_thirdsem = [x + barWidth for x in r_train]
    r_fourthsem = [x + barWidth for x in r_ship]


    # Make the plot
    plt.bar(r_firstsem, bars_firstsem, color='#7f6d5f', width=barWidth, edgecolor='white',label="First Semester")
    plt.bar(r_secondsem, bars_secondsem, color='#557f2d', width=barWidth, edgecolor='white', label="Second Semester")
    plt.bar(r_thirdsem, bars_thirdsem, color='#2d7f5e', width=barWidth, edgecolor='white', label="Third Semester")
    plt.bar(r_fourthsem, bars_fourthsem, color='#510f2f', width=barWidth, edgecolor='white', label="Fourth Semester")



    # Add xticks on the middle of the group bars
    plt.xlabel('Arrivals by Semestert', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], [ "2011", "2012", "2013" , "2014" , "2015"])

    # Create legend & Show graphic
    plt.legend()
    plt.show()
