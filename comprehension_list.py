pares = [x for x in range(1, 21) if x%2 == 0]
impares = [x for x in range(1, 21) if x%2 != 0]
print(pares)
print(impares)

# obtener los impares dependiendo el rango entre un numero x que define el extremo izq y un lado y que define el der

def impares(izq, der):
    impares = [x for x in range(izq, der+1) if x%2 != 0]
    return impares

print(impares(int(input("Escriba el limite izquierdo: ")), int(input("Escriba el limite derecho: "))))