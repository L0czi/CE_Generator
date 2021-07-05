import csv
import json
import data_base as db
import sys
sys.path.append('C:/Users/Marcin/Desktop/python_stuff/CE_GENERATOR/Layout')

import layout as l

def query_all_data_from_csv():
    '''Function read data about radiators from example.csv file and return it'''
    with open('example.csv', encoding='utf-8') as data:
        csv_data = csv.reader(data)
        data_lines = list(csv_data)
        return data_lines[1:]

def compare_data(rad_from_csv, rad_from_db):
    '''Function compera radiators from .csv file and from data base'''
    result = [item for item in rad_from_csv if item[0] not in rad_from_db]
    return result

def generate_CE(rad_from_db, lang):

    try:
        for radiator in rad_from_db:

            radiator_model = radiator[0]
            radiator_family = radiator[1].replace('_',' ')
            CE_type = radiator[3]
            date = radiator[4]
            declaration_name = 'DeclarationCE_'+ radiator_model.replace('/','_')+'_'+lang+'.pdf'


            CE_pdf = l.language_switcher(lang)
            CE_pdf.add_page()

            #generate document header
            CE_pdf.document_header()
            #generate document content
            CE_pdf.document_content(radiator_model, radiator_family, CE_type)
            #generate document footer
            CE_pdf.document_footer(date)
            #save file
            CE_pdf.output('Printed_Declarations/' + declaration_name)

            print(f"{declaration_name} is generate succesfully")

    except PermissionError:
        print("\nWARNING!!!")
        print(f"{declaration_name} is open in another aplication and can't be generate.")
        print("Please close another aplication and try again")

def query_all_data_from_db():
    '''read all data stored in rad.db'''
    try:
        query = "SELECT * from radiators_CE"
        data = db.read_data(query)

        if data == []:
            raise ValueError

    except ValueError:
        print('Data base is empty')

    else:
        result = [rad[1:] for rad in data]
        return result

def query_data_from_db(query, value):
    '''query data from rad.db'''
    try:
        data = db.read_data(query,value)

        if data == []:
            raise ValueError

    except ValueError:
        print(f"Given {value} not found in data base")

    else:
        result = [rad[1:] for rad in data]
        return result

def query_data_into_db(input_data):
    '''validate input data to rad.db and quering them'''
    try:
        if input_data == []:
            raise ValueError

        db.upload_data(input_data)

    except ValueError:
        print("No new radiators to add")





