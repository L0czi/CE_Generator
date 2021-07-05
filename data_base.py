'''modul for manage database'''
import sqlite3
import datetime


def read_data(sql_fetch_query, value=None):
    '''Function wich query data from rad.db'''
    try:
        sqliteConnection = sqlite3.connect('rad.db')
        cursor = sqliteConnection.cursor()

        if value==None:
            cursor.execute(sql_fetch_query)

        else:
            cursor.execute(sql_fetch_query,value)

        record = cursor.fetchall()

        return record
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()

def upload_data(input_data):
    '''Function upload new radiator from input list to data base'''
    try:
        sqliteConnection = sqlite3.connect('rad.db')
        cursor = sqliteConnection.cursor()
        query = "INSERT INTO radiators_CE VALUES (NULL,:Name, :Family, :Model_Type, :CE_Type, :Sign_Date, :CP)"

        for item in input_data:

            if len(item)<5:
                print(f"Missing argument for {item}. Check data in .csv file ")
                continue

            name = item[0]
            familly = item[1]
            model_type = item[2]
            CE_type = item[3]
            sign_date = datetime.date.today()
            cp_number = item[4]

            input_data_tuple = (name, familly, model_type, CE_type, sign_date, cp_number)
            cursor.execute(query, input_data_tuple)

            sqliteConnection.commit()
            print(f'Radiator model: {name} add to database with success')

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into table.", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()

