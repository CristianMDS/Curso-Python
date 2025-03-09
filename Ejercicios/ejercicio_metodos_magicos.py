"""
        CLASE 49
Implementar un archivo que contenga funciones para gestionar empleados.
    1. Funciones para agregar y eliminar empleados en una LISTA.
    2. Un bloque "if __name__ == __main__" que ejecute el escript directamente
        'python3 ejercicio_metodos_magicos.py'
"""

class Management_Employees:
    def __init__(self, list: list[str]):
        self.list = list

    def add_employee(self, name_employee: str):
        self.list.append(name_employee)

    def del_employee(self, name_employee: str):
        self.list.remove(name_employee)

    def show_list_employees(self) -> list:
        return self.list
    
employees_list = ['Cristian', 'David', 'Mora', 'Saenz']
obj = Management_Employees(employees_list)
print(f"Lista de empleados inicial: \n {obj.show_list_employees()}")
obj.add_employee('Maria')
print(f"Lista de empleados actualizada (Agregado): \n {obj.show_list_employees()}")
obj.del_employee('David')
print(f"Lista de empleados actualizada (Eliminado): \n {obj.show_list_employees()}")

# if __name__ == __main__:

if __name__ == "__main__":
    print("\n -- Ahora usando los metodos magicos. -- \n")
    employees_list = ['Cristian', 'David', 'Mora', 'Saenz']
    obj = Management_Employees(employees_list)
    print(f"Lista de empleados inicial: \n {obj.show_list_employees()}")
    obj.add_employee('Maria')
    print(f"Lista de empleados actualizada (Agregado): \n {obj.show_list_employees()}")
    obj.del_employee('David')
    print(f"Lista de empleados actualizada (Eliminado): \n {obj.show_list_employees()}")

# Output: Toca hacerlo con el comando "python archivo.py" en el curso usan "python3 archivos.py"
    # El numero 3 que hace referencia a la version no permite que el sistema reconozca python