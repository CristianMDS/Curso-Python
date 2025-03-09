x = 4

def modify_global():
    global x # se declara x como variable global
    x += 8 # se modifica el valor de x
    print(f'valor de X modificado: {x}') # se imprime el valor de x modificado

modify_global()