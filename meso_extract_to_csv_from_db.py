import csv
import MySQLdb
import mysql.connector
import xlrd

def meso_exctract_to_csv_from_db():

    with open('D:/Python_Project_Compilers/meso_2011_a.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2011_a")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow( { "number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6] })

        csvfile.close


    with open('D:/Python_Project_Compilers/meso_2011_b.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2011_b")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow( { "number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6] })

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2011_c.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2011_c")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow( { "number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6] })

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2011_d.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2011_d")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow( { "number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6] })

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2012_a.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2012_a")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2012_b.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2012_b")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2012_c.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2012_c")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2012_d.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2012_d")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2013_a.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2013_a")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2013_b.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2013_b")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2013_c.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2013_c")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2013_d.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2013_d")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2014_a.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2014_a")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2014_b.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2014_b")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2014_c.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2014_c")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2014_d.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2014_d")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2015_a.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2015_a")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2015_b.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2015_b")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2015_c.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2015_c")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close

    with open('D:/Python_Project_Compilers/meso_2015_d.csv', 'w') as csvfile:
        fieldnames = ['number', 'nation', 'plane', 'train', 'ship', 'car','total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="TOURISM_DATABASE")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        # Get the cursor, which is used to traverse the database, line by line
        mycursor.execute("SELECT number, nation, plane, train, ship, car, total FROM  meso_2015_d")
        select_result = mycursor.fetchall()

        writer.writeheader()

        for x in select_result:
            writer.writerow({"number" : x[0], "nation" : x[1], "plane" : x[2], "train" : x[3], "ship" : x[4], "car" : x[5] , "total" : x[6]})

        csvfile.close