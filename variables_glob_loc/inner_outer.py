x = 'global'
def outer_function ():
    x = 'encapsulado'

    # inner function
    def inner_function (): # ahora se define una funcion interna
        x = 'local'
        print('inner:', x) # se imprime el valor de x en la funcion interna (local)

    inner_function() # se ejecuta la funcion inicial
    print('outer:', x) # se imprime el valor de x dentro de la funcion inicial (encapsulado)

outer_function() # primero se ejecuta esta funcion
print('global:', x) # finalmente se imprime el valor de x global (global)