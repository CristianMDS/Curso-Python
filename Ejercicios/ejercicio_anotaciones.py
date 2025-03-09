"""
Este es un ejercicio que consiste en filtrar los salarios de los empleados bien sea mayor o menor que.

 - Clase: N° 41
 - Nota: El ejercicio representa un diccionario, sin embargo al no estar compuesto (Con keys) 
        que inicialicen cada "sub diccionario" no se usan corchetes como un dict, si no que se 
        representa como una lista.
"""

import json
class Employees:

    dict_employees: dict
    dict_temp: dict

    def __init__(self, dictionary: dict):
        self.dict_employees = dictionary
        self.dict_temp = {}

    def read_dict (self) -> dict:
        for employee in self.dict_employees:
            if(employee["salary"] <= 2500):
                self.dict_temp[employee["name"]] = {
                    "age": employee["age"],
                    "salary": employee["salary"]
                }
            
        return self.dict_temp
        
employees = [
    {"name": "Cristian", "age": 25, "salary": 2500},
    {"name": "David", "age": 25, "salary": 2700},
    {"name": "Mora", "age": 25, "salary": 2300},
    {"name": "Saenz", "age": 25, "salary": 3000}
]

obj = Employees(employees)
print(json.dumps(obj.read_dict(), indent=4))

"""
Aquí un ejemplo de como funciona este ejercicio si es una lista.
"""

class list_Employees:

    dict_employees: list

    def __init__(self, dictionary: list):
        self.dict_employees = dictionary

    def read_dict_list(self) -> json:
        dict_temp_list = list(filter(lambda x: x["salary"] > 2500, self.dict_employees))
        return json.dumps(dict_temp_list) # output formato json (Es mas legible).

employees = [
    {"name": "Cristian", "age": 25, "salary": 2500},
    {"name": "David", "age": 25, "salary": 2700},
    {"name": "Mora", "age": 25, "salary": 2300},
    {"name": "Saenz", "age": 25, "salary": 3000}
]

obj = list_Employees(employees)
print(obj.read_dict_list())
