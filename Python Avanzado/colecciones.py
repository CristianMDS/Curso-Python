"""  ¡ COLLECTIONS !

 + Es una libreria que agrega modulos a python

1. from collections import deque

 Es un (DeQueue) con este se pueden agregar elementos al inicio o al final de una lista
    list = deque()
    Inicio -> list.appendlef()
    Final -> list.append() (Default)

2. from collections import defaultdict



3. from collections import namedtuple

 Funciona para darle nombre a una tupla 
    Persona = namedtuple('Persona', 'nombre edad')
    persona = Persona(nombre='Juan', edad=25)
    print(persona.nombre)  # Salida: Juan


4. from collections import Counter

 Cuenta los elementos de una lista y retorna las llaves agrupadas con sus cantidades.
    cuenta = Counter(['manzana', 'pera', 'manzana'])
    print(cuenta)  # Salida: Counter({'manzana': 2, 'pera': 1})


"""
from collections import defaultdict
from collections import Counter
from collections import deque
delivery_queue = deque()



def count_orders(orders: list[str]) -> defaultdict:

    product_count = defaultdict(int)
    for product in orders:
        product_count[product] += 1

    return product_count

def counter_orders(orders:list[str]) -> Counter:
    return Counter(orders)

orders = ['laptop', 'mouse', 'laptop', 'keyboard', 'mouse', 'laptop']
print(f'\n Usando defaultdict: {count_orders(orders)}')
print(f'\n Usando Counter: {counter_orders(orders)}')

def manage_delivery_orders (orders: list[str]) -> deque:
    global delivery_queue
    delivery_queue = deque(orders)
    return delivery_queue

def add_in_start_delivery_orders (order: str) :
    global delivery_queue
    delivery_queue.appendleft(order)

def add_in_end_delivery_orders (order: str):
    global delivery_queue
    delivery_queue.append(order)

def show_delivery_orders() -> deque :
    global delivery_queue
    return delivery_queue

orders = ['order_1', 'order_2']
print(manage_delivery_orders(orders))
add_in_start_delivery_orders('order_0')
add_in_end_delivery_orders('order_3')
print(show_delivery_orders())


    
