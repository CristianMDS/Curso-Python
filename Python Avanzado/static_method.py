class Order:
    @staticmethod
    def calculate_tax(amount:float, tax_rate: float):
        return round(amount * (tax_rate/100), 2)
    
# Para utilizar los metodos staticos lo hacemos directamente llamando a la clase
print(f'Los impuestos de {12598.56} dolares son del {15.9}% dandonos como resultado: {Order.calculate_tax(12598.56, 15.9)}')
        
class Another_Order:
    global_discount = 10

    def __init__(self, amount: float):
        self.amount = amount

    @classmethod
    def update_global_discount(cls, discount: float):
        cls.global_discount = discount
    

Another_Order.update_global_discount(18)
print(Another_Order.global_discount)