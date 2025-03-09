class Vehiculo:
    def __init__(self, marca, tipo, color, precio):
        self.marca = marca
        self.tipo = tipo
        self.color = color
        self.precio = precio
        self.disponible = True

class Cliente:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.vehiculo = ''

    def comprar(self, vehiculo):
            vehiculo.disponible = False
            self.vehiculo = vehiculo.marca
            self.presupuesto -= vehiculo.precio
            print(f"\n -- El cliente {self.nombre} ha comprado '{vehiculo.tipo} {vehiculo.marca}' de color {vehiculo.color}")

    def mirarBilletera(self):
        print(f"\n -+ Tu presupuesto actual es de: $ {self.presupuesto}")

    def vehiculoNuevo(self):
        print(f"\n {self.nombre} tu nuevo vehiculo es un {self.vehiculo}")

class Consecionario:
    def __init__(self):
        self.clientes = []
        self.vehiculos = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"\n + El cliente {cliente.nombre} fue creado exitosamente")

    def registrar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"\n + El vehiculo {vehiculo.marca} de tipo {vehiculo.tipo} fue creado exitosamente")

    def vender_vehiculo(self, vehiculo, cliente):
        if vehiculo in self.vehiculos:
            if vehiculo.disponible == True:
                if cliente.presupuesto >= vehiculo.precio:
                    cliente.comprar(vehiculo)
                    self.vehiculos.remove(vehiculo)
                else:
                    print(f"\n !!UPS¡¡ tu presupuesto de $ {cliente.presupuesto} NO alcanza para comprar el vehiculo {vehiculo.marca} con un precio de $ {vehiculo.precio}")
            else:
                print(f"\n El vehiculo {vehiculo.marca} ya no esta disponible")
        else: 
            print(f"\n -> Este vehiculo {vehiculo.marca} ya no se encuentra disponible")

    def listar_vehiculos(self):
        print("\n --> Lista de vehiculos disponibles en el consecionario: ")
        for vehiculo in self.vehiculos:
            if vehiculo.disponible == True:
                print(f"| Marca: {vehiculo.marca} | Tipo: {vehiculo.tipo} |  Color: {vehiculo.color} |  Precio: $ {vehiculo.precio} | ")

## Aqui inicia la instancia de obj

# clientes
cliente1 = Cliente("Cristian", 2000)
cliente2 = Cliente("Maria", 3500)
cliente3 = Cliente("Santiago", 5500)

# vehiculos
vehiculo1 = Vehiculo("Renault", "Sedan", "Azul", 1500)
vehiculo2 = Vehiculo("Chevrolet", "Camioneta", "Rojo", 3500)
vehiculo3 = Vehiculo("Ford", "Camioneta", "Verde", 2500)
vehiculo4 = Vehiculo("Huskvarna", "Motocicleta", "Blanca", 1500)
vehiculo5 = Vehiculo("Foton", "Camion", "Blanco", 5500)

# consecionario
consecionario = Consecionario()

# Agregamos clientes 
consecionario.registrar_cliente(cliente1)
consecionario.registrar_cliente(cliente2)

# Agregamos vehiculos
consecionario.registrar_vehiculo(vehiculo1)
consecionario.registrar_vehiculo(vehiculo2)
consecionario.registrar_vehiculo(vehiculo3)
consecionario.registrar_vehiculo(vehiculo4)
consecionario.registrar_vehiculo(vehiculo5)

# Un Cliente llega al consecionario y revisa la lista de vehiculos
consecionario.listar_vehiculos()

# Ahora el cliente revisa su presupuesto
cliente1.mirarBilletera()

# Le gusto el Ford
consecionario.vender_vehiculo(vehiculo3, cliente1)

# revisa la lista de vehiculos
consecionario.listar_vehiculos()

# Como no alcanzo toco ir por el Renault
consecionario.vender_vehiculo(vehiculo1, cliente1)

# El cliente mira para ver si le alcanza para los dulces
cliente1.mirarBilletera()

print("\n Cambio de historia: Cliente 2")
# Entra el cliente numero 2
cliente2.mirarBilletera()

# Mira la lista
consecionario.listar_vehiculos()

# Le gusto el camion Foton
consecionario.vender_vehiculo(vehiculo5, cliente2)

# Como no alcanzo toco para la Ford
consecionario.vender_vehiculo(vehiculo3, cliente2)

# El cliente 2 revisa si le alcanzo para la gaseosa
cliente2.mirarBilletera()

# Los clientes revisan sus vehiculos.
cliente1.vehiculoNuevo()
cliente2.vehiculoNuevo()

# llego un cliente 3 a preguntar si aun tienen la Ford
consecionario.vender_vehiculo(vehiculo3, cliente3)

# Como no esta disponible decide llevarse la motocicleta
consecionario.vender_vehiculo(vehiculo4, cliente3)

# la lista quedo asi
consecionario.listar_vehiculos()
