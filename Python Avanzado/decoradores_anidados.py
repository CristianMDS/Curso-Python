def acelerar(func):
    def wrapped():
        func() # dependiendo de donde se coloque esta funcion { acelerar(argumento) } 
                # se ejecutara la funcion principal { debajo del decorador @ }
        print("acelerando...")

    return wrapped

@acelerar
def carro():
    print("Carro encendido...")


carro()