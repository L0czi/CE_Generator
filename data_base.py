"""modul for manage database"""
import sqlite3
import datetime


def read_data(sql_fetch_query, value=None):
    """Function wich query data from rad.db"""
    try:
        sqliteConnection = sqlite3.connect("rad_data_base.db")
        cursor = sqliteConnection.cursor()

        if value == None:
            cursor.execute(sql_fetch_query)

        else:
            cursor.execute(sql_fetch_query, value)

        record = cursor.fetchall()

        cursor.close()

        return record

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()


def upload_data(input_data):
    """Function upload new radiator from input list to data base"""
    try:
        sqliteConnection = sqlite3.connect("rad_data_base.db")
        cursor = sqliteConnection.cursor()
        query = "INSERT INTO CE_radiators VALUES (NULL, :Name, :Family, :Model_Type, :CP, :CE_Type, :Report_num, :Signaturer, :Sign_Date)"

        for item in input_data:

            if len(item) < 7:
                print(f"Missing argument for {item}. Check data in .csv file ")
                continue

            name = item[0]
            familly = item[1]
            model_type = item[2]
            cp_number = item[3]
            ce_type = item[4]
            report_num = item[5]
            signaturer = item[6]
            sign_date = datetime.date.today()

            input_data_tuple = (
                name,
                familly,
                model_type,
                cp_number,
                ce_type,
                report_num,
                signaturer,
                sign_date,
            )
            cursor.execute(query, input_data_tuple)

            sqliteConnection.commit()
            print(f"Radiator model: {name} add to database with success")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into table.", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
