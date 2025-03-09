a = [1,2,3,4]
b = a
print("Estado original del arreglo a y la variable b usando ( a ) sin el metodo slice")
print(a)
print(b)
print("\nA continuacion elimino el primer campo de la variable 'a': \n")
del a[0]
print(a)
print(b)
print("\nComo ( b ) es igual a lo que hay dentro del arreglo ( a ) al eliminar se borra en ( b )\n")
print(id(a)) # Aqui se demuestra que es el mismo espacio en memoria
print(id(b)) # Aqui se demuestra que es el mismo espacio en memoria
print("\nPara evitar esto, se agrega el 'metodo slice' indicando que el arreglo ( c ) es igual al \narreglo ( a ) desde el inicio al final usando [:]\n")
a = [1,2,3,4]
c = a[:]
del a[0]
print(a)
print(c)

