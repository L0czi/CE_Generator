import csv
import data_base as db
from fpdf import Template
import time


def query_all_data_from_csv():
    """Function read data about radiators from example.csv file and return it"""
    with open("example.csv", encoding="utf-8") as data:
        csv_data = csv.reader(data, delimiter=";")
        data_lines = list(csv_data)
        return data_lines[1:]


def query_lang_from_csv(lang):

    with open("Layout/lang/" + lang + ".csv", encoding="utf-8") as data:
        csv_data = csv.reader(data, delimiter=";")
        data_lines = list(csv_data)
        result = [item[0] for item in data_lines]
        return result


def compare_data(rad_from_csv, rad_from_db):
    """Function compera radiators from .csv file and from data base"""
    result = [item for item in rad_from_csv if item[0] not in rad_from_db]
    return result


def generate_CE(input_list, lang):

    start = time.perf_counter()
    counter = 0

    try:
        for rad in input_list:

            templates = rad[4].split(",")
            language = query_lang_from_csv(lang)

            for temp in templates:

                title = (
                    "Declaration_"
                    + rad[0].replace("/", "_")
                    + "_"
                    + lang
                    + "_"
                    + temp
                    + ".pdf"
                )

                f = Template(format="A4", title=title)
                f.parse_csv("Layout/temp/" + temp + ".csv")
                f.add_page()

                f["rad_model"] = rad[0]
                f["rad_name"] = rad[1]
                f["report_num"] = rad[5]
                f["signer"] = rad[6]
                f["date"] = rad[7]

                f["line1"] = language[0]
                f["line2"] = language[1]
                f["line3"] = language[2]
                f["line4"] = language[3]
                f["line5"] = language[4]
                f["line6"] = language[5]
                f["line7"] = language[6]
                f["line8"] = language[7]
                f["line9"] = language[8]
                f["line10"] = language[9]
                f["line11"] = language[10]
                f["line12"] = language[11]
                f["line13"] = language[12]
                f["line14"] = language[13]

                f["company_logo"] = "Layout/Zehnder.png"
                f["sign"] = "Layout/sign.png"

                f.render("Printed_Declarations/" + title)
                print(f"{title} is generated succesfully")
                counter += 1

    except PermissionError:
        print("\nWARNING!!!")
        print(f"{title} is open in another aplication and can't be generate.")
        print("Please close another aplication and try again")

    stop = time.perf_counter()
    print("\n")
    print(f"Generation time: {stop-start:0.3f}")
    print(f"Generated declarations: {counter}")


def query_all_data_from_db():
    """read all data stored in rad.db"""
    try:
        query = "SELECT * from CE_radiators"
        data = db.read_data(query)

        if data == []:
            raise ValueError

    except ValueError:
        print("Data base is empty")

    else:
        result = [rad[1:] for rad in data]
        return result


def query_data_from_db(query, value):
    """query data from rad.db"""
    try:
        data = db.read_data(query, value)

        if data == []:
            raise ValueError

    except ValueError:
        print(f"Given {value} not found in data base")

    else:
        result = [rad[1:] for rad in data]
        return result


def query_data_into_db(input_data):
    """validate input data to rad.db and quering them"""
    try:
        if input_data == []:
            raise ValueError

        db.upload_data(input_data)

    except ValueError:
        print("No new radiators to add")
