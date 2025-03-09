"""
 Buscar los pares de zapatos con la misma talla
"""

class Zapatos:
    def organizeShoes(self, shoes):
        if len(shoes) == 0:
            return []
        
        shoes = sorted(shoes, key=lambda x: x['size'])
        size_tmp = 0
        type_tmp = ''
        pear_list = list()
        for pear in shoes:
            if size_tmp != '' and type_tmp != '' and size_tmp == pear['size']:
                if size_tmp == pear['size'] and type_tmp != pear['type']:
                    pear_list.append(pear['size'])
                    size_tmp, type_tmp = '', ''

            else:
                size_tmp = pear['size']
                type_tmp = pear['type']
        
        return pear_list

shoes = [
  { 'type': 'I', 'size': 38 },
  { 'type': 'R', 'size': 38 },
  { 'type': 'I', 'size': 38 },
  { 'type': 'I', 'size': 38 },
  { 'type': 'R', 'size': 38 },
]

obj = Zapatos()
print(obj.organizeShoes(shoes))
