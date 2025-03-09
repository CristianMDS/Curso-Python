"""
* Verificacion de tareas
* Calculo del costo total
* Procesamiento de pago
"""

import asyncio, time, random, multiprocessing

# Funcion asincrona para verificar el inventario
async def check_inventary(item):
    print(f"Verificando inventario {item} ...")
    # Simulacion de proceso
    await asyncio.sleep(random.randint(1, 5))
    print(f"Inventario verificado")
    # Simular disponibilidad
    return random.choice([True, False])

async def process_payment(order_id):
    print(f"Procesando servicio de pago {order_id}....")
    await asyncio.sleep(random.randint(1, 8))
    print(f"Pago procesado para la orden: {order_id}")
    return True

# Funcion 
def calculate_total(items):
    print(f"Calculando el costo total para {len(items)} articulos..... ")
    time.sleep(10)
    total = sum(item['price'] for item in items)
    print(f"Costo total calculado: {total}")

async def process_order(order_id, items):
    print(f"Inicia el procesamiento de la orden: {order_id}")
    # Verificar inventario
    inventory_check = [check_inventary(item['price']) for item in items]
    invetory_result = await asyncio.gather(*inventory_check)

    if not all(invetory_result):
        print(f"La ordern {order_id} fue cancelada")
    
    with multiprocessing.Pool() as pool:
        total = pool.apply(calculate_total, (items,))

    payment_result = await process_payment(order_id)

    if payment_result:
        print(f"Orden: {order_id} completada con exito. Total: {total}")
    else:
        print(f"Error al procesar el pago de la orden {order_id}")

async def main():
    orders = [
        {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 50}]},
        {'order_id': 2, 'items': [{'name': 'Teclado', 'price': 80}, {'name': 'Monitor', 'price': 300}]},
        {'order_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'Funda', 'price': 20}]}
    ]

    # Procesar multiples ordenes
    tasks = [process_order(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())


