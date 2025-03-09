# funciones lambda utilizadas para no especificar nombre para las funciones, como una funcion arrow en js
sumar = lambda a, b: a + b
print(sumar(10,12))

numeros = range(1, 11)
cuadrado = list(map(lambda x: x**2, numeros)) # maps ejecuta la operacion usando numeros como elementos iterables
print(cuadrado)

# impares
# filter utiliza la condicional para aplicar en numero la busqueda de impares
impares = list(filter(lambda x: x%2 != 0, numeros)) 
print(impares)

pares = list(filter(lambda x: x%2 == 0, numeros))
print(pares)