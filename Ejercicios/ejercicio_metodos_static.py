class Delivery:
    @staticmethod
    def verify_amount(list: list):
        try:
            if str(list[0]) == '':
                raise ValueError('El pedido debe tener un nombre')
            if float(list[1]) >= 50:
                print("El pedido es valido")
            elif float(list[1]) < 50:
                print("El pedido no cumple la regla de minimo $50")
        except ValueError as e:
            print(f"Error: {e}")

Delivery.verify_amount(['Compras', 75]) # Output: El pedido es valido
Delivery.verify_amount(['Compras', 45]) # Output: El pedido no cumple la regla de minimo $50
Delivery.verify_amount(['', 50]) # Output: Error: El pedido debe tener un nombre

import json
        
class Order_Discount:
    global_discount = 0

    
    @classmethod
    def __init__(self, shopping_list: dict):
        self.shopping_list = shopping_list

    @classmethod
    def __apply_shopping_list(self):
        self.shopping_list["global_discount"] = self.global_discount

    @classmethod
    def _show_list(self) -> json:
        print(json.dumps(self.shopping_list, indent=4))

    @classmethod
    def update_global_discount(cls, discount: float):
        cls.global_discount = discount
        cls.__apply_shopping_list()

list = {
    "global_discount": 0,
    "products": {
        "shampoo": {
            "price": 12,
            "quantity": 1
        },
        "soap": {
            "price": 5,
            "quantity": 15
        }
    }
}

Order_Discount(list)
Order_Discount.update_global_discount(12)
Order_Discount._show_list()
