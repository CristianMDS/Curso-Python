class Orden_Regalos:
    def fix_packages(self, packages):
        if len(packages) == 0:
            return ''
        
        lista_tmp = []
        parentesis = []
        for letter in packages:
            lista_tmp.append(letter)
            if lista_tmp.count('(') == 1 and letter == '(':
                lista_tmp = []
            elif letter == ')':
                parentesis = lista_tmp[:-1]
                tmp, tmx = '('+''.join(lista_tmp), ''.join(parentesis)
                packages = packages.replace(tmp, tmx[::-1])
                break

        if '(' in packages:
            return self.fix_packages(packages)
    
        return packages


packages = '(abc(def(ghi)))'
obj = Orden_Regalos()
print(obj.fix_packages(packages))