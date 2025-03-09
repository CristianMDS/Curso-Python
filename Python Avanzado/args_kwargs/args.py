"""
 Se utiliza el simbolo reservado * seguido de la palabra args, para indicar
 que no tenemos serteza de cuantos argumentos van a ingresar al metodo.
"""
from collections import deque

def concatenando_texto(*args) -> deque:
    texto_completo = deque(args)
    texto_completo = ''.join(texto_completo)
    return texto_completo

print(concatenando_texto('Hola', ',', ' como', ' ', 'estas', '?')) # fijarse que en la funcion pase 6 argumentos.

    