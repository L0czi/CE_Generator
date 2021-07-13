import csv
import data_base as db
from fpdf import Template
import time


def read_data_from_csv(file_name):
    """common function for reading data from csv files"""
    with open(file_name, encoding="utf-8") as data:
        csv_data = csv.reader(data, delimiter=";")
        list_data = list(csv_data)
        return list_data


def compare_data(rad_from_csv, rad_from_db):
    """Function compera radiators from given .csv input file and stored in data base"""
    result = [item for item in rad_from_csv if item[0] not in rad_from_db]
    return result


def generate_CE(rad_list, lang):
    """Function generate a ce_declaration from given template, language option and data about products stored in .db"""
    start = time.perf_counter()
    counter = 0

    try:
        for rad in rad_list:

            # read all possible template
            # type is stored in rad_list and can be diffrent for next rad
            # second loop is prepared for cases whan there is more than one
            # template assign to radiator
            templates = rad[4].split(",")

            # read a proper language template based on given "lang"
            lang_template_name = "Layout/lang/" + lang + ".csv"
            lang_template = read_data_from_csv(lang_template_name)
            language = [item[0] for item in lang_template]

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
                # set up a template
                f = Template(format="A4", title=title)
                template_name = "Layout/temp/" + temp + ".csv"
                f.parse_csv(template_name)
                f.add_page()

                # fill all prepared gaps in template
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
