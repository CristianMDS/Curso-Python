employees = [
    {"name": "Juan", "age": 28, "salary": 3500},
    {"name": "María", "age": 32, "salary": 4200},
    {"name": "Carlos", "age": 25, "salary": 3100},
    {"name": "Ana", "age": 40, "salary": 5000},
    {"name": "Luis", "age": 30, "salary": 3900},
]

"""
    Parameters: 
    dict: list, 
    salary: int

    Retorna:
    list: Lista de empleados cuyo salario es mayor al salario ingresado
"""
def get_employees(dict, salary):
    return list(filter(lambda x: x["salary"] > salary, dict))

search_salary = int(input("Ingrese el salario a buscar: "))
print(f'\n {get_employees(employees, search_salary)}')




    

