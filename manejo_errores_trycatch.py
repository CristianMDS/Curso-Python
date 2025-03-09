try:
    x = True
    while x == True:
        try:
            numero = int(input("\nPor favor ingresa un numero: "))
            operacion = 12 / numero
            print(operacion)
            
            respuesta = str(input("\nEscriba [Y] para volver a ejecutar o presione cualquier otra letra Para detener: "))
            x = True if respuesta == "Y" or respuesta == "y" else False


        except ZeroDivisionError as e:
            print("Error: A ocurrido un error de operacion")
            print(f"El error es: {e}")
        except ValueError as e:
            print("Error: A ocurrido un error con el valor ejecutado")
            print(f"El error es: {e}")
except NameError as ex:
    print("Error: Problemas con alguna variable")
    print(f"El error es: {ex}")