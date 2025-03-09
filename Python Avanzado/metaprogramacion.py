"""
La metaprogramación en Python es una técnica que permite a los programas manipular o generar 
código durante su ejecución. Esto se puede lograr a través de varias funcionalidades del lenguaje, 
como las clases, los decoradores, las funciones de alto orden y los metaclases.
"""

class multiplyFactor:
    def __new__(cls, factor: int): # En este caso se coloca primero __new__ por buena practica
        print(f"Se crea una instancia con el valor adquirido previamente -> {factor}")
        return super(multiplyFactor, cls).__new__(cls)
    
    def __init__(self, factor: int):
        print(f"Inicializamos el factor -> {factor}")
        self.factor = factor

    def __call__(self, number: int) -> int:
        return number * self.factor
    
# Inicializamos el obj y agregamos el "factor" de __init__
obj = multiplyFactor(5)

# Inicializamos una variable con el resultado y pasamos a nuetro objeto el numero multiplicador.
resultado = obj(10)
print(resultado)