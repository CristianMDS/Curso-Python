to_do = ['caminar', 'correr', 'saltar lazo']
print(to_do)
numeros = [1,2,3,4, 'cinco']
print(numeros)

mix = [1, 2, 3.45, "esto es una cadena", True, [1, 2, 3]]

print(mix)
print(mix[2])
print(mix[:-1]) # Esto es conocido como un slice

# insertar datos
print(mix)
mix.append(["a", "b", [5, 6]])
print(mix)

# insertar en una posicion especifica
print(mix)
mix.insert(1, "elemento")
print(mix)

# obtener el index de un elemento conocido
print(f"Posicion: {mix.index("elemento")}")

# mostrar la lista al reves
print(f"Lista original: {mix}")
mix.reverse()
print(f"Lista al reves: {mix}")

# mostrar el numero minimo y maximo de un arreglo
numbers = [1, 2, 3, 100, 76, 56, 25]
print(f"Numeros: {numbers}")
print(f"Ordenados: {sorted(numbers)}")
print(f"Maximo: {max(numbers)}")
print(f"Minimo: {min(numbers)}")

# eliminar un elemento
print(mix)
del mix[-1] # eliminamos el ultimo elemnto (El arreglo dentro del arreglo)
print(mix)

# eliminar un slice de elementos
print(mix)
del mix[4:] # eliminamos el ultimo elemnto (El arreglo dentro del arreglo)
print(mix)

# eliminar un toda la lista
print(mix)
del mix # eliminamos el ultimo elemnto (El arreglo dentro del arreglo) print(mix) # no imprime algo que no existe
