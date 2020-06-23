import csv
import xlrd
import pandas as pd
import re

def meso_exctract_csv_from_excel():

    filename = 'D:\Python_Project_Compilers/meso_2011_a.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΜΑΡ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2011_a_xl.csv"


    with open(csvfilepath, 'w+', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2011_b.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΙΟΥΝ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2011_b_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2011_c.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΣΕΠ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2011_c_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2011_d.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΔΕΚ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2011_d_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2012_a.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΜΑΡ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2012_a_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2012_b.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΙΟΥΝ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2012_b_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2012_c.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΣΕΠΤ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2012_c_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2012_d.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΔΕΚ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2012_d_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2013_a.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΜΑΡ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2013_a_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(74, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2013_b.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΙΟΥΝ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2013_b_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(74, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2013_c.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΣΕΠ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2013_c_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2013_d.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΔΕΚ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2013_d_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()
    filename = 'D:\Python_Project_Compilers/meso_2014_a.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΜΑΡ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2014_a_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(76, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2014_b.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΙΟΥΝ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2014_b_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2014_c.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΣΕΠΤ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2014_c_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2014_d.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΔΕΚ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2014_d_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2015_a.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΜΑΡ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2015_a_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2015_b.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΜΑΡ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2015_b_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(77, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2015_c.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΣΕΠΤ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2015_c_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(77, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue

            writer.writerow(sh.row_values(rownum))

    csvfile.close()

    filename = 'D:\Python_Project_Compilers/meso_2015_d.xls'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('ΔΕΚΕΜ')

    csvfilepath = "D:\Python_Project_Compilers/meso_2015_d_xl.csv"


    with open(csvfilepath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for rownum in range(75, sh.nrows):
            if ( not(re.search("\d\." , str(sh.cell(rownum, 0))))):
                continue
            writer.writerow(sh.row_values(rownum))

    csvfile.close()

