import asyncio

async def process_data(data):
    print(f"Procesando {data}...")
    # simular operacion
    await asyncio.sleep(10)
    print(f"{data} procesado.")
    return data*2

async def main():
    print('Inicio')
    result = await process_data('archivo.txt')
    print(f"Resultado: {result}")

asyncio.run(main())