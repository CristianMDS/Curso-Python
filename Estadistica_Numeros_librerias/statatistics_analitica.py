import statistics
import csv

path = 'C:/Users/crist/Desktop/Curso Python/Estadistica_Numeros_librerias/ventas.csv'

#Leer el contenido del archivo
with open(path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    pago_mensual = {}
    for row in csv_reader:
        mes = row['mes']
        pago = int(row['total_ventas'])
        pago_mensual[mes] = pago
    
ventas = list(pago_mensual.values())
print(ventas)

# MEDIA 
media = statistics.mean(ventas)
print(f"La media de todos los datos es: {media}")

# MEDIANA
mediana = statistics.median(ventas)
print(f"La mediana de todos los datos es: {mediana}")

# MODA
moda = statistics.mode(ventas)
print(f"La moda de todos los datos es: {moda}")

# Desviacion Estandar
desviacion = statistics.stdev(ventas)
print(f"La desviacion de todos los datos es: {desviacion}")

# Varianza
varianza = statistics.variance(ventas)
print(f"La varianza de todos los datos es: {varianza}")

# Maximas y minimas
maxima = max(ventas)
minima = min(ventas)
print(f"La maxima de todos los datos es: {maxima}")
print(f"La minima de todos los datos es: {minima}")

# rango 
rango = maxima - minima
print(f"La rango de todos los datos es: {rango}")


