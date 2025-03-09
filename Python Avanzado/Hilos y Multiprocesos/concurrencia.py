"""
Hilos, sin embargo, cada vez que uno carga otro inicia, 
por esta razon pueden tardar mas en ejecutarse
"""

import threading, time

#Funcion que simula procesamiento de una solicitud
def processing_request(request_id):
    print(f"procesando solicitud {request_id}")
    time.sleep(5)
    print(f"solicitud {request_id} Terminada")

threads = []

for i in range(5):
    # Creamos cada hilo, 
    #  - El argumento "target" es nuestr funcion objetivo, 
    #  - El argumento "args" hace referencia a los argumentos de esa funcion y 
    #       la coma (,) que sigue es por que es un iterable
    thread = threading.Thread(target=processing_request, args=(i,))
    threads.append(thread) # Agregamos los hilos a la lista.
    thread.start() # Inicia cada hilo.

# Esperar que los hilos terminen
for thread in threads:
    # Asegura que cada hilo termine
    thread.join()

print('Todos los hilos finalizados.')