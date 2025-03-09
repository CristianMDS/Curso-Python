def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def dividir(a,b):
    return a / b

def multiplicar(a,b):
    return a * b

def seleccion(a, signo, b):
    if signo == "+":
        return sumar(a, b)
    elif signo == "-":
        return restar(a, b)
    elif signo == "/":
        return dividir(a, b)
    elif signo == "*":
        return multiplicar(a, b)
    else:
        return "Esta funcion no esta en la calculadora"

operacion = input("Escriba su operacion \nNOTA: Solo se puede \nSumar ( + ), \nRestar( - ), \nMultiplicar( * ), \nDividir( / ) \n->  ")
op = operacion.strip()

if ' ' in op:
    print("entro al in")
    op = operacion.split(' ')
else:
    op = list(operacion)

print("imprimiendo el op-> ",op)
print(seleccion(int(op[0]), str(op[1]), int(op[2])))
