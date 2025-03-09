x = 13
if x > 12 or x >= 12:
    print(f"Es mayor o igual la verdad no se dimelo tu: {x}")
    respuesta = bool(input("Es Mayor: ( True ) Es igual: ( False ) "))  # "Pregunta al usuario"
    resultado = "Es Mayor" if respuesta == True else "Es igual"  # "operador ternario"
    print(resultado)
elif x < 12:
    print("x es menor que 12")
else:
    print("Nop")