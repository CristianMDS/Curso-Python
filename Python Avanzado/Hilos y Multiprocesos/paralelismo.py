"""
Hilos simultaneamente funcionando, esto depende de la capacidad de 
    procesamiento (Nucleos) [multiprocesos]
"""

import multiprocessing
import time


#Funcion que calcula el cuadrado de un numero
def calculate_square(n):
    return n*n


if __name__ == '__main__':
    start_time = time.time()
    numbers = list(range(1, 100000))

    # Crear un pool

    with multiprocessing.Pool() as pool:
        result = pool.map(calculate_square, numbers)

        print(f"resultados: {result}")


        # Guarda el tiempo de finalización
        end_time = time.time()

        # Calcula el tiempo de ejecución
        execution_time = round(end_time - start_time, 3)
        if execution_time > 60:
            s = "minutos"
            execution_time = execution_time / 60
        else:
            s = "segundos"    
        print(f"El tiempo de ejecución es: {execution_time} ", s)