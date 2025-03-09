"""
                            CLASE 51
    Crear una funcion que reciba una cantidad variable de productos y precios,
    que calcule el total y aplique los descuentos (opcional [si se proporciona como un argumento con nombre { kwarg }])

"""
from datetime import datetime
import json

class Ventas:
    def __init__(self, *args, store, client, date):
        self.store = store
        self.client = client
        self.date = date
        self.products = args

    def show_products(self) -> json:
        final_ticket = {}
        total_price = 0
        total_discount = 0
        count = 0
        final_ticket[self.client] = {
            "store": self.store,
            "date": self.date.isoformat(),
            "productos": {}
        }

        lista = list(self.products)

        for i, fila in enumerate(lista):
            for j, valor in enumerate(fila):
                product = str(lista[i][j][0])
                price = float(lista[i][j][1])
                discount = float(lista[i][j][2])
                total_price += price
                total_discount += discount
                discount_name = str("Discoount_"+str(count)) 
                final_ticket[self.client]["productos"].update({
                    product: price,
                    discount_name: discount
                })
                count += 1

        final_ticket[self.client]["productos"].update({
            "total_discounts": (total_discount)
        })
        
        final_ticket[self.client]["productos"].update({
            "total_price": (total_price - total_discount)
        })

        return json.dumps(final_ticket, indent=4)


# La variable ticket se utiliza para **kwargs, se utiliza desempaquetando los argumentos.
ticket = {
    "store": "Mercado zapatoca",
    "client": "Cristian David Mora Saenz",
    "date": datetime.now().date()
}

# La variable products se utiliza para *args
products = [
    ["manzana",30.5, 10.8],
    ["Leche", 50.5, 0.1]
]

obj = Ventas(products, **ticket)
print(obj.show_products())