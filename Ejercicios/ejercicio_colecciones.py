"""
Implementa un sistema de gestion de pedidos utilizando colecciones y enumeraciones
"""
from collections import defaultdict, Counter
from enum import Enum
import json

class state_package (Enum):
    PREPARE = 1
    SEND = 2
    DELIVERED = 3

class delivery_system:
    orders: dict

    def __init__(self, orders: dict):
        self.orders = orders

    def show_state_delivery(self) -> defaultdict :
        status = defaultdict(str) # defaultdict type string
        for key in self.orders.keys():
            order = self.orders[key]["state_package"]
            if (order == state_package.PREPARE):
                status[key] = {
                    "addres": self.orders[key]["address"],
                    "state_package": 'Preparando paquete',
                    "code": self.orders[key]["code"]
                }
            elif (order == state_package.SEND):
                status[key] = {
                    "addres": self.orders[key]["address"],
                    "state_package": 'Paquete enviado',
                    "code": self.orders[key]["code"]
                }
            elif (order == state_package.DELIVERED):
                status[key] = {
                    "addres": self.orders[key]["address"],
                    "state_package": 'Paquete entregado',
                    "code": self.orders[key]["code"]
                }
            
        return status
    
    """ 
        def show_especific_orders (self, especific_orders: dict) -> list:
            lista = list()
            for key in self.orders.keys():
                code = self.orders[key]["code"]
                order = Counter(especific_orders[code])
                lista.append(order)
            
            return lista
         
    """ # Output: [Counter({'Duff': 4, 'Donut': 2}), Counter({'Bible': 3}), Counter({'Glasses': 1})]

    def show_especific_orders (self, especific_orders: dict) -> defaultdict:
        especific_order = defaultdict(str)
        for key in self.orders.keys():
            code = self.orders[key]["code"]
            especific_order[key] = {
                "code": code,
                "address": self.orders[key]["address"],
                "products": Counter(especific_orders[code])
            }

        return especific_order


    
orders = {
    "Homer Simpson" : {"address": "742 Evergreen springfield", "state_package": state_package.PREPARE, "code": 1},
    "Ned Flanders" : {"address": "741 Evergreen springfield", "state_package": state_package.SEND, "code": 2},
    "Luann Van Houten" : {"address": "743 Evergreen springfield", "state_package": state_package.DELIVERED, "code": 3},
}

especific_orders = {
    1: ["Duff", "Duff", "Duff", "Duff", "Donut", "Donut"],
    2: ["Bible", "Bible", "Bible", "Bible"],
    3: ["Glasses"]
}
    
obj = delivery_system(orders)
print(f'\n ¡ESTADO DEL PEDIDO! \n {json.dumps(obj.show_state_delivery(), indent=4)} \n')
print(f'\n ¡DESCRIPCION DE LOS PEDIDOS! \n {json.dumps(obj.show_especific_orders(especific_orders), indent= 5)}')