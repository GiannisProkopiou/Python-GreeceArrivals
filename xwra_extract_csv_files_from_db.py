import csv
import MySQLdb
import mysql.connector
import xlrd

def xwra_exctract_csv_files_from_db():

    with open('D:/Python_Project_Compilers/xwra_2011_a.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2011_a")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow( { "number" : x[0], "nation" : x[1], "year_before" : x[2], "year_now" : x[3], "year_difference" : x[4], "year_analogy" : x[5] })

        csvfile.close


    with open('D:/Python_Project_Compilers/xwra_2011_b.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2011_b")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow( { "number" : x[0], "nation" : x[1], "year_before" : x[2], "year_now" : x[3], "year_difference" : x[4], "year_analogy" : x[5] })

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2011_c.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2011_c")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow( { "number" : x[0], "nation" : x[1], "year_before" : x[2], "year_now" : x[3], "year_difference" : x[4], "year_analogy" : x[5] })

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2011_d.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2011_d")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow( { "number" : x[0], "nation" : x[1], "year_before" : x[2], "year_now" : x[3], "year_difference" : x[4], "year_analogy" : x[5] })

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2012_a.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2012_a")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2012_b.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2012_b")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2012_c.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2012_c")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2012_d.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2012_d")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2013_a.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2013_a")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2013_b.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2013_b")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2013_c.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2013_c")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2013_d.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2013_d")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2014_a.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2014_a")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2014_b.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2014_b")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2014_c.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2014_c")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2014_d.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2014_d")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2015_a.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2015_a")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2015_b.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2015_b")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2015_c.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2015_c")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close

    with open('D:/Python_Project_Compilers/xwra_2015_d.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'year_before', 'year_now', 'year_difference', 'year_analogy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, year_before, year_now, year_difference, year_analogy FROM xwra_2015_d")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number": x[0], "nation": x[1], "year_before": x[2], "year_now": x[3], "year_difference": x[4],
                             "year_analogy": x[5]})

        csvfile.close