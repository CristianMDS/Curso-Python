a = 10
b = 2

operacion_Pemdas_1 = a + b ** 2; 
operacion_Pemdas_2 = (a + 3) * b ** 2 / 8 - 1; # (13) * 2 ** 2 / 8 - 1 = (13) * 4 / 8 - 1 = (52) / 8 - 1 = 6,5 - 1 = 5,5 

print("SUMA: ", a + b)
print("RESTA: ", a - b)
print("DIVISION: ", a / b)
print("PARTE ENTERA DE LA DIVISION: ", a // b)
print("MULTIPLICACION: ", a * b)
print("POTENCIA: ", a ** b)
print("MODULACION: ", a % b)
print("PEMDAS_1: ", operacion_Pemdas_1) # Potencia Exponente Multiplicacion Division Adicion Sustraccion
print("PEMDAS_2: ", operacion_Pemdas_2) # Potencia Exponente Multiplicacion Division Adicion Sustraccion
print(a > b) # true
print(a < b) # false