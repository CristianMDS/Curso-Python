class OrganizarInventario:
    def organizeInventory(self, inventary):
      if len(inventary) == 0:
        return {}
      
      product_sorted = {}
      inventary = sorted(inventary, key=lambda x: x['category'])

      for product in inventary:
        if product['category'] not in product_sorted:
          product_sorted[product['category']] = {product['name']: product['quantity']}
        else:
          if product['name'] in product_sorted[product['category']]:
            product_sorted[product['category']][product['name']] += product['quantity']
          else:
            product_sorted[product['category']][product['name']] = product['quantity']


      return product_sorted



            
    



inventary2 = [
  { 'name': 'doll', 'quantity': 5, 'category': 'toys' },
  { 'name': 'car', 'quantity': 3, 'category': 'toys' },
  { 'name': 'ball', 'quantity': 2, 'category': 'sports' },
  { 'name': 'car', 'quantity': 2, 'category': 'toys' },
  { 'name': 'racket', 'quantity': 4, 'category': 'sports' }
]

obj = OrganizarInventario()
obj.organizeInventory(inventary2)