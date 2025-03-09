import csv

filePath = 'C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/customers-100.csv'
archivo_actualizado = 'C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/customers-100_Update.csv'

with open(filePath, mode='r') as csv_file:
    csv_reading = csv.DictReader(csv_file)
    nombre_columnas = csv_reading.fieldnames + ["nombre_completo"]

    with open(archivo_actualizado, mode='w', newline='') as csv_file_updated:
        csv_writer = csv.DictWriter(csv_file_updated, fieldnames = nombre_columnas)
        csv_writer.writeheader() # Escribir los encabezados

        for row in csv_reading:
            row["nombre_completo"] = str(row["First Name"]), str(row["Last Name"])
            csv_writer.writerow(row)

with open(archivo_actualizado, mode='r', encoding='utf-8') as csv_read:
    csv_reader = csv.DictReader(csv_read)
    print(" > -- Clientes -- < ")
    for row in csv_reader:
        print(f"| Nombre completo: {row["nombre_completo"]} - Telefono: {row["Phone 1"]} - Ciudad: {row["City"]} | \n")


        