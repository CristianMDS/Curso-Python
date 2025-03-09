class People:
    # name: str
    # age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        # Devuelve una representacion amigable con el usuario. Ej.
        return f"People: name = {self.name}, age = {self.age} "
    
    def __repr__(self) -> str:
        # Devuelve una representacion tecnica del objeto.
        return f"People:(name={self.name}, age={self.age}) "
    
    def __eq__(self, other_people) -> bool:
        # Compara si dos objetos (Personas) son iguales
        return self.name == other_people.name and self.age == other_people.age
    
    def __lt__ (self, other_people) -> bool:
        # Compara si un valor (Edad) es menor al del objeto comparado.
        return self.age < other_people.age
    
    def __add__ (self, other_people) -> bool:
        # Suma los valores (Edad) y los retorna
        return self.age + other_people.age

p1 = People("Cristian", 25)
p2 = People("Maria", 25)
p3 = People("Lina", 22)

print(p1) # __str__
print(repr(p2)) # __repr__
print(p1 == p2) # __eq__
print(p3 < p1) # __lt__
print(p1 + p2) # __add__


"""

OTRAS ANOTACIONES

1. Inicialización y Representación
    __init__: Inicializa una nueva instancia.
    __new__: Controla la creación de una instancia antes de inicializarla.
    __del__: Ejecuta lógica al eliminar una instancia.
    __repr__: Devuelve una representación formal del objeto.
    __str__: Devuelve una representación informal legible del objeto.

2. Operadores Aritméticos
    __add__: Suma (+).
    __sub__: Resta (-).
    __mul__: Multiplicación (*).
    __truediv__: División (/).
    __floordiv__: División entera (//).
    __mod__: Módulo (%).
    __pow__: Potencia (**).
    __neg__: Negativo (-obj).

3. Operadores de Comparación
    __eq__: Igualdad (==).
    __ne__: Desigualdad (!=).
    __lt__: Menor que (<).
    __le__: Menor o igual que (<=).
    __gt__: Mayor que (>).
    __ge__: Mayor o igual que (>=).

4. Contenedores e Iteradores
    __getitem__: Acceso por índice (obj[i]).
    __setitem__: Asignación por índice (obj[i] = valor).
    __delitem__: Eliminación por índice (del obj[i]).
    __len__: Tamaño (len(obj)).
    __iter__: Devuelve un iterador para el objeto.
    __next__: Devuelve el siguiente elemento del iterador.
    __contains__: Verifica si un elemento está contenido (x in obj).

5. Representaciones Numéricas
    __int__: Conversión a entero (int(obj)).
    __float__: Conversión a flotante (float(obj)).
    __bool__: Conversión a booleano (bool(obj)).

6. Gestión de Contextos
    __enter__: Lógica al entrar en un contexto (with obj:).
    __exit__: Lógica al salir de un contexto.
    
7. Operadores Bit a Bit
    __and__: AND bit a bit (&).
    __or__: OR bit a bit (|).
    __xor__: XOR bit a bit (^).

8. Manejo de Atributos
    __getattr__: Acceso a atributos inexistentes.
    __setattr__: Asignación de atributos (obj.attr = valor).
    __delattr__: Eliminación de atributos (del obj.attr).


"""