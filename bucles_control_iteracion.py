arr = [1,2,3,4,5]
for i in arr:
    print(i)

print("Aqui inicia el while \n")

x = 0
while x < len(arr):
    print(arr[x])
    x += 1

# arreglos de 2 dimensiones

arr_2d = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10]]

print(f"Arreglo en 2d {arr_2d} \n")
for i in arr_2d:
    print("Esto es i: ", i)
    for j in i:
        print("Esto es j:", j)
        if j == 3:
            break