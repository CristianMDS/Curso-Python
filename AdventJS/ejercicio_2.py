"""
Santa Claus 🎅 quiere enmarcar los nombres de los niños buenos para decorar su taller 🖼️, pero el marco debe cumplir 
unas reglas específicas. Tu tarea es ayudar a los elfos a generar este marco mágico.

Reglas:

- Dado un array de nombres, debes crear un marco rectangular que los contenga a todos.
- Cada nombre debe estar en una línea, alineado a la izquierda.
- El marco está construido con * y tiene un borde de una línea de ancho.
- La anchura del marco se adapta automáticamente al nombre más largo más un margen de 1 espacio a cada lado.
"""
class Marco:
    def __init__(self):
        self.names = []
    
    def createFrame(self, names):
        if len(names) == 0:
            return '*'
        
        espacios = 0
        count = 0
        asteriscos = '****'
        final = ''
        for name in names:
            if count < len(name):
                count = len(name) # Count es el numero de letras mas grande

        espacios = count
        # agrego a los * iniciales la cantidad de asteriscos de la palabra mas grande
        while count > 0:
            asteriscos += '*'
            count -= 1


        final += asteriscos
        for name in names:
            count = espacios

            if len(name) == count:
                final += f"\n* {name} *"
            else:
                new_count = count - len(name)
                while new_count > 0:
                    name += ' '
                    new_count -= 1

                final += f"\n* {name} *"
        final += "\n" + asteriscos

        return final

tablero = ["aqwdqwdqwdqwd", "bb", "ccc", "dddd", "fffff"]
obj = Marco()
print(obj.createFrame(tablero))
