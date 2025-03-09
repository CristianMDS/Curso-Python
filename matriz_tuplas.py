matriz = [[1,2,3], 
        [4,5,6]]

print(matriz[1][2]) # matriz[x (filas)][y (Columnas)]

# listas o arreglos 3dimensiones 
arr_3d = [[[1,2],[3,4]], 
          [[5,6],[7,8]]]
# x = fila, y = columna, z = corchete sub_interno -> objetivo = 7
print(arr_3d[1][1][0])

# tuplas (A diferencia de las matrices las tuplas no pueden ser modificadas)

tupla = ((1,2,3), (4,5,6))
print(tupla)
print(type(tupla))

tupla[1][2] = 7 # error
print(tupla)

