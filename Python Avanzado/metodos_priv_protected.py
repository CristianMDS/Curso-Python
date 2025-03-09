"""

        CLASE 52
 - Protected: Para crear un metodo protejido debemos colocar un guion bajo [ _metodo_protegido ]
 - Private: Pra crear un metodo privado debemos agregar dos guion bajo al inicio [ __metodo_privado ]
"""
import random
class Protected_Private:
    def __init__(self, name: str, lastname: str):
        self._name = name # variable protejida
        self._lastname = lastname # variable protejida
        self.__pass = random.randint(111111, 9999999) # variable privada

    def __metodo_privado(self): # metodo privado
        print(f"ten mucho cuidado esta es tu contraseña {self.__pass}")

    def _metodo_protejido(self): # metodo protejido
        print(f"Hola mundo para {self._name} {self._lastname}")
        desicion = input("¿Quieres ver tu contraseña? [Y/N]")
        if desicion in ('Y', 'y'):
            return self.__metodo_privado()
        elif desicion in ('N', 'n'):
            return f"Entendido sr {self._name}"

    def metodo_publico(self): # metodo publico
        print("Hola")
        desicion = input("¿Quieres ver tu nombre? [Y/N]")
        if desicion in ('Y', 'y'):
            return self._metodo_protejido()
        elif desicion in ('N', 'n'):
            return f"Entendido sr {self._name}"
        
obj = Protected_Private('Cristian', 'Mora')
obj.metodo_publico()


    