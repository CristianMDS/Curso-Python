def divide (a:int, b:int) -> float:
    if not isinstance(a, int) and isinstance(b, int):
        raise TypeError('Los dos parametros deben ser números enteros.')
    
    if b == 0:
        raise ValueError('No se puede dividir por 0')
    
    return a/b

try:
    print("¡ BIENVENIDO ! Vamos a divivir las manzanas para los niños")
    a = int(input("Ingresa el numero de manzanas (disponibles): "))
    b = int(input("Ingresa el numero de niños: "))
    print(f'A cada niño le tocan de a {divide(a, b)} manzana(s)')

except (TypeError, ValueError) as e:
    print(f'Error: {e}')
