id_1: int = 101 
id_2: int = 101 
cliente: str = "Cristian"

id_total = id_1 + id_2

print(f'{id_total} del cliente {cliente}')

# Output: 202 del cliente Cristian

""" Ejemplo con funciones  """

def suma(a: int, b: int) -> int:
    return a + b

print(suma(2, 3))

""" Ejemplo con clases """

class Employee:
    name: str
    age: int
    salary: float

    def __init__ (self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduccion (self) -> str:
        return f"Hi my name is {self.name}, i have {self.age} years old"
    
obj1 = Employee('Cristian', 25, 2500.00)
print(obj1.introduccion())