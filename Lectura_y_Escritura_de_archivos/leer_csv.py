import csv

# Leer csv
# with open('C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/customers-100.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         print(row)


# Agregar un nuevo valor

new_customer = {
    'Index': 101,
    'Customer Id': '2354a0E336A91A2',
    'First Name': 'Cristian',
    'Last Name': 'Mora',
    'Company': 'Mora - Tech',
    'City': 'Bogotá',
    'Country': 'Colombia',
    'Phone 1': '+57 3179678477',
    'Phone 2': '+57 3568756412',
    'Email': 'mora@cristian.com',
    'Subscription Date': '2024-11-22',
    'Website': 'prueba.cristianmora.dev'
}

with open('C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/customers-100.csv', mode='w', newline='') as csv_file:
    print("\n")
    csv_writer = csv.DictWriter(csv_file, fieldnames= new_customer.keys())
    csv_writer.writerow(new_customer)

with open('C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/customers-100.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print(" > --  Clientes -- < ")
    for row in csv_reader:
        print(f"\n | Cliente: {str(row['First Name']), str(row['Last Name'])} - Telefono: {row['Phone 1']} - Ciudad: {row['City']} |")

