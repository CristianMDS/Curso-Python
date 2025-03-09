"""
Funciona similar que los *args, sin embargo utilizamos **kwargs
este "parametro" le indica a nuestra funcion que nos pueden pasar diferentes 
tamaños de argumentos pero nos van a indicar sus kw (Key Words).
"""

def empleados(**kwargs) -> str:
    concat = ''
    empleados = dict
    for key, value in kwargs.items():
        concat += f"key: [{key}] - value: [{value}] \n"


    return concat
    

print(empleados(name='Cristian', age=25, birthday="02/04/2000", games="GTA-V, BTF4, Fortnite"))

