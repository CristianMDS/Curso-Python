def calculate_average(numbers):
    """
    Esta funcion calcula el promedio de una lista de numeros

    Parameters:
    numbers (list): Lista de numeros enteros o flotantes

    Retorna:
    float: Promedio de la lista de numeros
    """
    return sum(numbers) / len(numbers)


print(calculate_average([1, 2, 3, 4, 5]))  # 3.0