import os

# Obtener la ruta actual
cwd = os.getcwd()
print(f"Nos encontramos en la ruta {cwd}")

# Buscar los elementos dentro de un directorio
"""buscar_html = [f for f in os.listdir('.') if f.endswith('.html')]
    print("Los archivos html son: ", buscar_html)"""

# Cambiar nombre
"""os.rename(buscar_html[0], 'index.php')"""

# Buscar los elementos dentro de un directorio
"""buscar_html = [f for f in os.listdir('.') if f.endswith('.php')]
    print("Los archivos html son: ", buscar_html)"""

print(os.cpu_count()) # cuenta el numero de procesadores
# print(os.environ)
print(os.system('py diccionarios.py'))

