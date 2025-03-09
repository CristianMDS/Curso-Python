class Arbol:
    # Por alguna extraña razon en el advent ornament es la altura y height el ornamento
    def createXmasTree(self, ornament, height): 
        if height == 0 or ornament == '':
            return ''
        
        x = (height*2) - 1
        y = height
        arbol = [['' for _ in range(x)] for _ in range(y)]
        base_del_arbol = [['_' for _ in range(x)] for _ in range(2)] 

        n = len(arbol)
        m = len(arbol[0])

        columna = y - 1
        # Declarar con el elemento la posicion inicial
        i, j = 0, columna
        arbol[i][j] = ornament

        # Agregar la base del arbol
        base_del_arbol[i][j] = '#'
        base_del_arbol[i+1][j] = '#'
        

        # Diagonal principal se deja la fila en 0 
        i, j = 0 + 1, columna + 1 
        while i < n and j < m:
            arbol[i][j] = ornament
            i += 1 
            j += 1

        # Diagonal secundaria se deja la fila en 0
        i, j = 0 + 1, columna - 1 
        while i < n and j >= 0:
            arbol[i][j] = ornament
            i += 1 
            j -= 1

        # Tapar la parte baja de las diagonales.
        count = n - 1
        while count > 0:
            # count hace las veces de una X y el resultado de index las de Y
            fil = count
            col = arbol[count].index(ornament)

            while col <= m:
                if arbol[fil][col+1] == '':
                    arbol[fil][col+1] = ornament
                    col += 1
                elif arbol[fil][col+1] == ornament:
                    break

            count -= 1

        # Pasar el arreglo a plano
        txt = ""
        for sublista in arbol:
            for elemento in sublista:
                if elemento == '':
                    txt += '_'
                else:
                    txt += elemento
            
            txt += "\n"
            
        cont = 0
        for sublista in base_del_arbol:
            for elemento in sublista:
                txt += elemento

            if cont != 1:
                txt += "\n"

            cont += 1


        return txt

obj = Arbol()
print(obj.createXmasTree('$', 5))