import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk
import csv
import pandas as pd
import requests
import openpyxl
import xlrd
import MySQLdb
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pandas import DataFrame
import re
from tkinter import *
from tkinter.ttk import *

from Script_for_excel_files import Script_for_excel_files
from xwres_excel_to_mysql import xwres_excel_to_mysql
from meso_excel_to_mysql import meso_excel_to_mysql
from xwra_extract_csv_files_from_db import xwra_exctract_csv_files_from_db
from graph_data_from_db import graph_data_from_db
from graph_data_from_excel import graph_data_from_excel
from meso_extract_to_csv_from_db import meso_exctract_to_csv_from_db
from xwra_extract_csv_from_excel import xwra_exctract_csv_from_excel
from meso_extract_csv_from_excel import meso_exctract_csv_from_excel
from graph_max_by_year import graph_max_by_year
from graph_total_arrivals_by_year import graph_total_arrivals_by_year
from graph_meso_by_semester import graph_meso_by_semester
from graph_total_by_mean import graph_total_by_mean


root = tk.Tk()
# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("200x200")

def print_graph_max_by_year():

    bars_max_to_print = graph_max_by_year()

    # Toplevel object which will
    # be treated as a new window
    MaxWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    MaxWindow.title("Semester Window")

    # sets the geometry of toplevel
    MaxWindow.geometry("1000x1000")

    figure_max = plt.Figure(figsize=(6, 5), dpi=100)
    ax_max = figure_max.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure_max, MaxWindow)
    chart_type.get_tk_widget().pack()
    # df = df[['First Column', 'Second Column']].groupby('First Column').sum()
    # df.plot(kind='Chart Type such as bar', legend=True, ax=ax)
    ax_max.set_title('Graph Max By Year')

    # set width of bar
    barWidth = 0.25

    # set height of bar
    #bars_max = [max_2011, max_2012, max_2013, max_2014, max_2015]

    # Set position of bar on X axis
    r1 = np.arange(len(bars_max_to_print))

    # Make the plot
    plt.bar(r1, bars_max_to_print, color='#7f6d5f', width=barWidth, edgecolor='white')  # label=nation_max_2011)

    # Add xticks on the middle of the group bars
    plt.xlabel('Most Valuable Nations', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars_max_to_print))],
               ["2011: \n" + str(bars_max_to_print.nation_max_2011), "2012: \n" + str(bars_max_to_print.nation_max_2012),
                "2013: \n" + str(bars_max_to_print.nation_max_2013),
                "2014: \n" + str(bars_max_to_print.nation_max_2014), "2015: \n" + str(bars_max_to_print.nation_max_2015)])

    # Create legend & Show graphic
    plt.legend()
    plt.show()

def print_total_arrivals_by_year():

    total_arrivals_by_year = graph_total_arrivals_by_year()

    # Toplevel object which will
    # be treated as a new window
    YearWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    YearWindow.title("Semester Window")

    # sets the geometry of toplevel
    YearWindow.geometry("1000x1000")

    figure_total_arrivals = plt.Figure(figsize=(6, 5), dpi=100)
    ax_year = figure_total_arrivals.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure_total_arrivals, YearWindow)
    chart_type.get_tk_widget().pack()
    # df = df[['First Column', 'Second Column']].groupby('First Column').sum()
    # df.plot(kind='Chart Type such as bar', legend=True, ax=ax)
    ax_year.set_title('Graph Total Ariivals By Year')

    # data
    # df_total_arrivals_by_year = pd.DataFrame({'x': ("2011", "2012", "2013", "2014", "2015"), 'y': (
    #     total_arrivals_2011, total_arrivals_2012, total_arrivals_2013, total_arrivals_2014, total_arrivals_2015)})

    # plot
    plt.plot('x', "y", data=total_arrivals_by_year, linestyle='-', marker='o')
    plt.show()

def print_total_by_mean():

    bars_plane_to_print, bars_train_to_print, bars_shipto_print, bars_car_to_print = graph_total_by_mean()

    # Toplevel object which will
    # be treated as a new window
    MeanWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    MeanWindow.title("Semester Window")

    # sets the geometry of toplevel
    MeanWindow.geometry("1000x1000")

    figure_total_by_mean = plt.Figure(figsize=(6, 5), dpi=100)
    ax_mean = figure_total_by_mean.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure_total_by_mean, MeanWindow)
    chart_type.get_tk_widget().pack()
    # df = df[['First Column', 'Second Column']].groupby('First Column').sum()
    # df.plot(kind='Chart Type such as bar', legend=True, ax=ax)
    ax_mean.set_title('Graph Total By Mean')

    # set width of bar
    barWidth = 0.15

    # Set position of bar on X axis
    r_plane = np.arange(len(bars_plane_to_print))
    r_train = [x + barWidth for x in r_plane]
    r_ship = [x + barWidth for x in r_train]
    r_car = [x + barWidth for x in r_ship]

    # Make the plot
    plt.bar(r_plane, bars_plane_to_print, color='#7f6d5f', width=barWidth, edgecolor='white', label="Plane")
    plt.bar(r_train, bars_train_to_print, color='#557f2d', width=barWidth, edgecolor='white', label="Train")
    plt.bar(r_ship, bars_shipto_print, color='#2d7f5e', width=barWidth, edgecolor='white', label="Ship")
    plt.bar(r_car, bars_car_to_print, color='#510f2f', width=barWidth, edgecolor='white', label="Car")

    # Add xticks on the middle of the group bars
    plt.xlabel('Most Valuable Means of Transport', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars_plane_to_print))], ["2011", "2012", "2013", "2014", "2015"])

    # Create legend & Show graphic
    plt.legend()
    plt.show()

def print_graph_total_by_semester():

    bars_firstsem_to_print, bars_secondsem_to_print, bars_thirdsem_to_print, bars_fourthsem_to_print = graph_meso_by_semester()

    # Toplevel object which will
    # be treated as a new window
    SemWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    SemWindow.title("Semester Window")

    # sets the geometry of toplevel
    SemWindow.geometry("1000x1000")

    figure_total_by_semester = plt.Figure(figsize=(6, 5), dpi=100)
    ax_semester = figure_total_by_semester.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure_total_by_semester, SemWindow)
    chart_type.get_tk_widget().pack()
    # df = df[['First Column', 'Second Column']].groupby('First Column').sum()
    # df.plot(kind='Chart Type such as bar', legend=True, ax=ax)
    ax_semester.set_title('Graph Total By Semester')

    barWidth = 0.15

    # Set position of bar on X axis
    r_firstsem = np.arange(len(bars_firstsem_to_print))
    r_secondsem = [x + barWidth for x in r_firstsem]
    r_thirdsem = [x + barWidth for x in r_secondsem]
    r_fourthsem = [x + barWidth for x in r_thirdsem]

    # Make the plot
    plt.bar(r_firstsem, bars_firstsem_to_print, color='#7f6d5f', width=barWidth, edgecolor='white', label="First Semester")
    plt.bar(r_secondsem, bars_secondsem_to_print, color='#557f2d', width=barWidth, edgecolor='white', label="Second Semester")
    plt.bar(r_thirdsem, bars_thirdsem_to_print, color='#2d7f5e', width=barWidth, edgecolor='white', label="Third Semester")
    plt.bar(r_fourthsem, bars_fourthsem_to_print, color='#510f2f', width=barWidth, edgecolor='white', label="Fourth Semester")

    # Add xticks on the middle of the group bars
    plt.xlabel('Arrivals by Semester', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars_firstsem_to_print))], ["2011", "2012", "2013", "2014", "2015"])

    # Create legend & Show graphic
    plt.legend()
    plt.show()

canvas1 = tk.Canvas(root, width=300, height=650, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Python Project 2020', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


# def getExcel():
#     global read_file
#
#     import_file_path = filedialog.askopenfilename()
#     read_file = pd.read_excel(import_file_path)


Button_download_excel = tk.Button(text="     Download The Excel Files     ", command=Script_for_excel_files, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=Button_download_excel)

# Button_exctract_xwra_to_db = tk.Button(text='Exctract Xwra to MySQL', command=xwres_excel_to_mysql, bg='green', fg='white',
#                              font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 180, window=Button_exctract_xwra_to_db)

# Button_xwra_exctract_csv_files_from_db = tk.Button(text="     Extract Xwres CSV from DB     ", command=xwra_exctract_csv_files_from_db, bg='green', fg='white',
#                                font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 230, window=Button_xwra_exctract_csv_files_from_db)

# Button_meso_exctract_csv_files_from_db = tk.Button(text="     Extract Meso CSV from DB     ", command=meso_exctract_csv_files_from_db, bg='green', fg='white',
#                                font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 280, window=Button_meso_exctract_csv_files_from_db)

Button_xwra_exctract_csv_from_excel = tk.Button(text="     Extract Xwres CSV from Excel     ", command=xwra_exctract_csv_from_excel, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 330, window=Button_xwra_exctract_csv_from_excel)

Button_meso_exctract_csv_from_excel = tk.Button(text="     Extract Xwres CSV from Excel     ", command=meso_exctract_csv_from_excel, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 380, window=Button_meso_exctract_csv_from_excel)

# Button_graph_data_from_db = tk.Button(text="     Graph From DB Data     ", command=graph_data_from_db, bg='green', fg='white',
#                                font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 430, window=Button_graph_data_from_db)

Button_graph_data_from_excel = tk.Button(text="     Graph From Excel Data     ", command=graph_data_from_excel, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 480, window=Button_graph_data_from_excel)

# Button_meso_exctract_to_csv_from_db = tk.Button(text="     Graph From DB Data     ", command=meso_exctract_to_csv_from_db(), bg='green', fg='white',
#                                font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 530, window=Button_meso_exctract_to_csv_from_db)

Button_graph_max_by_year = tk.Button(text="     Graph Max By Year     ", command=print_graph_max_by_year, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 430, window=Button_graph_max_by_year)

Button_graph_total_arrivals_by_year = tk.Button(text="     Graph Total Arrivals By Year     ", command=print_total_arrivals_by_year, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 530, window=Button_graph_total_arrivals_by_year)

Button_graph_total_by_mean = tk.Button(text="     Graph Total By Mean     ", command=print_total_by_mean, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 280, window=Button_graph_total_by_mean)

Button_graph_total_by_semester = tk.Button(text="     Graph Total By Semester     ", command=print_graph_total_by_semester, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=Button_graph_total_by_semester)

# def convertToCSV():
#     global read_file
#
#     export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
#     read_file.to_csv(export_file_path, index=None, header=True)


# Button_exctract_meso_to_db = tk.Button(text='Exctract Meso to MySQL', command=meso_excel_to_mysql(), bg='green', fg='white',
#                              font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 580, window=Button_exctract_meso_to_db)




def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()


exitButton = tk.Button(root, text='       Exit Application     ', command=exitApplication, bg='brown', fg='white',
                       font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 630, window=exitButton)

root.mainloop()