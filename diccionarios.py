import json

numbers = {1:"uno", 2:"dos", 3:"tres"}

# Para acceder a estos elementos tenemos que usar sus llaves 1,2,3
print(numbers[1])
print(numbers[2],"\n")

informacion_personal = {"Nombres": "Cristian David", "Apellidos": "Mora Saenz", "Edad": 24}

# podemos acceder a todo el diccionario o simplemente a un elemento
print(informacion_personal)
print(informacion_personal["Apellidos"], "\n")

# podemos usar un diccionario dentro de otro para almacenar informacion

productos = {
    "Jabon":{"Marca": "Palmolive", "Precio": 2.5},
    "Shampoo":{"Marca": "Head & Shouders", "Precio": 12.5},
    "Pantalon":{"Marca": "Levi's", "Precio": 50.99}
}

print(productos)
print(f"PRODUCTOS \n - Jabon: {productos["Jabon"]} \n - Shampoo: {productos["Shampoo"]} \n - Blue Jean: {productos["Pantalon"]}")

# Para obtener las llaves o en este caso los productos
print("\n keys ", productos.keys())

# Para obtener los items o los elementos que componen el diccionario
print("\n items", productos.items)

# Para convertir el diccionario a json
print("\n JSON", json.dumps(productos))

# sumamos los precios de los productos y hacemos una lista de los productos comprados.
print("\n")
suma = 0
for claves in productos.keys():
    print(f" - Marca: {productos[claves]["Marca"]} $ {productos[claves]["Precio"]}")
    suma += productos[claves]["Precio"]

print(f"\nTotal de la compra: {round(suma, 2)}")