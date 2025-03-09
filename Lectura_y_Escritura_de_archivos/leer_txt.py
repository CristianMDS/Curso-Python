# Acciones de escritura y lectura de archivos en python
# 'r' -> Hace referencia reading por esta razon se lee lo que hay en el archivo
# 'a' -> Hace referencia append por lo que agregara al final del archivo lo que le indiquemos
# 'w' -> Hace referencia write pero en python esta funcion elimina todo lo del archivo y 
                                                    # sobreescribe en el la nueva informacion.


# Esta es una alternativa para leer las lineas dentro del archivo.

print("\n Ejemplo 1: \n")

with open('C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/cuento.txt', 'r', encoding='UTF-8') as file:
    for lines in file:
        print(lines.strip())

# Esta es la otra alternativa para leer las lineas, esta la almacena en una lista (Arreglo)

print("\n Ejemplo 2: \n")

with open('C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/cuento.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(lines)

# Agregar un elemento al final del archivo

print("\n Ejemplo 3: \n")

with open('C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/cuento.txt', 'a', encoding='UTF-8') as file:
    file.write("\n Web-page: https://arbolabc.com/fabulas-para-ni%C3%B1os/tio-tigre-y-tio-conejo")

with open('C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/cuento.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(lines[len(lines)-1]) # muestra la ultima linea (agregada) almacenada en la lista

# Sobre escribir el archivo

print("\n Ejemplo 4: \n")

print("De momento lo elimine para no ejecutar y sobreescribir el archivo")
# with open('C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/cuento.txt', 'w', encoding='UTF-8') as file:
    # file.write("Se borro todo y ahora solo queda esto")

with open('C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/cuento.txt', 'r', encoding='UTF-8') as file:
    for lines in file:
        print(lines)

# Ejercicio de la clase. 
# Contar el numero de lineas

print("\n Ejercicio: \n")

with open('C:/Users/crist/Desktop/Curso Python/Lectura_y_Escritura_de_archivos/cuento.txt', 'r', encoding='UTF-8') as file:
    lines = len(file.readlines())
    print(f"Cantidad de lineas: {lines}")



