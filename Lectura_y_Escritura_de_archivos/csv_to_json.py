import csv
import json

path_csv = 'C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/customers-100_Update.csv'
path_json = 'C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/customers-100_csv_to_json.json'

# Leer el contenido del csv
with open(path_csv, mode='r', encoding='utf-8') as csv_file:
    csv_reader = list(csv.DictReader(csv_file))

    with open(path_json, mode='w') as json_file:
        json.dump(csv_reader, json_file, indent=4)


        