# class Profesor:
#     def __init__(self, asignatura, nombre, zona_horaria):
#         self.asignatura = asignatura
#         self.nombre = nombre
#         self.zona_horaria = zona_horaria
        
#     def presentacion(self):
#         print(f"Hola soy el profesor {self.nombre}, yo dicto la asginatura de {self.asignatura} en la franja horaria de la {self.zona_horaria}")

# profesor1 = Profesor("Matematicas", "Miguel", "Tarde")
# profesor2 = Profesor("Sistemas", "Cristian", "Mañana")

# profesor1.presentacion()
# profesor2.presentacion()

class Ahorro:
    def __init__(self, nombre, cuenta, saldo_inicial):
        self.nombre = nombre
        self.cuenta = cuenta
        self.saldo_inicial = saldo_inicial
        self.estado = True

    def depositar(self, cuenta, monto):
        if self.estado == True:
            if self.cuenta == cuenta:
                self.saldo_inicial += monto
                print(f"El monto ingresado es $ {monto} y su saldo total es $ {self.saldo_inicial}")
            else:
                print("Error: La cuenta ingresada no existe")        
        else:
            print("Error: Su cuenta esta inactiva")

    def retirar(self, cuenta, monto):
        if self.estado == True:
            if self.cuenta == cuenta:
                if self.saldo_inicial >= monto:
                    self.saldo_inicial -= monto
                    print(f"Tu saldo final es $ {self.saldo_inicial} haz retirado $ {monto}")
                else:
                    print("Error: El saldo de tu cuenta es menor al monto que intentas retirar")
            else:
                print("Error: Esta cuenta no es correcta")
        else:
            print("Error: Tu cuenta esta desactivada")

    def congelarCuenta(self, cuenta):
        if self.cuenta == cuenta:
            self.estado = False
            print("Estado: Cuenta desactivada exitosamente")
        else:
            print("Error: Esta cuenta no existe")

    def descongelarCuenta(self, cuenta):
        if self.cuenta == cuenta:
            self.estado = True
            print("Estado: Cuenta activada exitosamente")
        else:
            print("Error: Esta cuenta no existe")

cuenta1 = Ahorro("Cristian Mora", 12345, 500)
cuenta1.depositar(12345, 100)
cuenta1.retirar(12345, 50)
cuenta1.congelarCuenta(12345)
cuenta1.depositar(12345, 500)
cuenta1.descongelarCuenta(12345)
cuenta1.depositar(12345, 400)