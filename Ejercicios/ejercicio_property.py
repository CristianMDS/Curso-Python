"""
Implementa una clase Producto

1 Utiliza @property para controlar el acceso y modificación del precio
2 Implementa validación para asegurarse de que el precio y el stock no puedan ser negativos
3 define un método que calcule el valor total del inventario
"""
import json
class Product:

    def __init__(self, employees: dict):
        self._employees = employees
        self.products = {}

    @property
    def manage_products(self) -> json:
        return json.dumps(self.products, indent=4)

    @manage_products.setter
    def manage_products(self, list: list) -> str:
        name_product = list[0]
        price_product = list[1]
        stock = list[2]
        employee = list[3]

        try:
            if not employee in self._employees:
                raise KeyError(f'Verifica tu nombre puede que este mal escrito o registrado [{employee}]')

            if self._employees[employee].get('rol') == 'admin':
                if price_product <= 0 or stock <= 0:
                    raise ValueError('El PRECIO y/o el STOCK del producto no puede ser negativo o 0')
                
                if not name_product in self.products:
                    self.products[name_product] = {
                        "price": price_product,
                        "stock": stock
                    }
                else:
                    self.products[name_product].update({
                        "price": price_product,
                        "stock": stock
                    })

                print(" Producto Creado exitosamente ")
            else:
                print(f"El usuario {employee} no tiene permitido crear productos")
                
        except (ValueError, KeyError) as e:
            print(f" --> Error: {e}")
        
    @manage_products.deleter
    def manage_products(self):
        print("\n Eliminados los productos")
        del self.products

    @property
    def manage_stock(self) -> int:
        count = 0
        for key, value in self.products.items():
            count += int(self.products[key].get('stock'))
        return count
    
    @manage_stock.setter
    def manage_stock(self, list: list) -> json:
        name_product = list[0]
        new_stock = list[1]

        self.products[name_product].update({
            "stock": new_stock
        })

        return json.dumps(self.products)


list_employees = {
    "Cristian": {"code":1, "rol":'employee'},
    "David": {"code":2, "rol":'admin'},
    "Omar": {"code":3, "rol":'employee'},
    "Felipe": {"code":4, "rol":'employee'},
    "Nicolas": {"code":5, "rol":'employee'}
}

obj = Product(list_employees)
print(obj.manage_products)

producto = ['Manzana', 5, 25, 'David']
obj.manage_products = producto

producto = ['Leche', 12, 10, 'David']
obj.manage_products = producto

producto = ['Arandanos', 5, 30, 'David']
obj.manage_products = producto

producto = ['Huevos', 15, 45, 'David']
obj.manage_products = producto

print("\n - Lista de productos (ACTUALIZADA) - \n", obj.manage_products)

print("Stock total de productos: ", obj.manage_stock)

new_stock = ['Huevos', 85]
obj.manage_stock = new_stock

print("\n - Lista de productos (ACTUALIZADA) - \n", obj.manage_products)

del obj.manage_products



