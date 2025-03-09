import json
import csv

path_json = 'C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/productos.json'
path_csv = 'C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/productos_json_to_csv.csv'

# JSON to CSV
with open(path_json, mode='r') as json_file:
    productos_reader = json.load(json_file)
    headers = productos_reader['productos'][0].keys()
    
    with open(path_csv, mode='w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers) # Esto es la declaracion de las cabeceras
        csv_writer.writeheader() # Aqui se plasman las cabeceras en el archivo.
        csv_writer.writerows(productos_reader['productos']) # Aqui se escriben los datos del json en el csv


# Visualizamos el archivo csv para ver como a quedado.

with open(path_csv, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(f"| Producto: {row['nombre']} - Categoria: {row['categoria']} - Precio: {row['precio']} - Disponibilidad: {row['stock']} |")



