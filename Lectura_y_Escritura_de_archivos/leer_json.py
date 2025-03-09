import json

path = 'C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/productos.json'

with open(path, mode='r', encoding='utf-8') as file:
    productos = json.load(file)

# Mostrar contenido
    print("<- PRODUCTOS ->")
for producto in productos['productos']:
    print(f"| Producto {producto['nombre']} - Precio: $ {producto['precio']} - Cantidad disponible: {producto['stock']} | \n")


# Agregar un elemento

nuevo_producto = {
    "nombre": "Six Pack Cerveza", "categoria": "Licores", "precio": 16000, "stock": 1000
}


with open(path, mode='r') as json_file:
    productos = json.load(json_file)
    productos['productos'].append(nuevo_producto) # Estoy agregando un nuevo producto dentro del 
                                                    # subdirectorio "productos" en el archivo json
                                                
print("Deberia agregar cerveza: \n")                                                
for producto in productos['productos']:
    print(f"| Producto: {producto['nombre']} - precio: $ {producto['precio']} - Disponibilidad: {producto['stock']} |\n")


with open(path, mode='w') as json_file:
    productos = json.dump(productos, json_file, indent=4)
    