# Usamos el ejemplo del consecionario

class Vehiculo:
    def __init__(self, marca, color, precio):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.disponible = True

    def get_precio(self):
        return self.precio
    
    def disponibilidad(self):
        if self.disponible:
            print(f"\n El vehiculo {self.marca} esta disponible")
        else:
            print(f"\n El vehiculo {self.marca} NO esta disponible")

    def encender_motor(self):
        raise NotImplementedError("Esto se ve en una clase especifica")
    
    def apagar_motor(self):
        raise NotImplementedError("Esto se ve en una clase especifica")

class Camion(Vehiculo):
    def encender_motor(self):
        if not self.disponible:
            return f"\n El motor del vehiculo {self.marca} esta encendido"
        else: 
            return f"\n El motor del vehiculo {self.marca} no esta encendido"
    
    def apagar_motor(self):
        if self.disponible:
            return f"\n El motor del vehiculo {self.marca} esta detenido"
        else: 
            return f"\n El motor del vehiculo {self.marca} no esta disponible"
        
class Motocicleta(Vehiculo):
    def encender_motor(self):
        if not self.disponible:
            return f"\n La motocicleta {self.marca} esta en marcha"
        else: 
            return f"\n La motocicleta {self.marca} no esta disponible"
    
    def apagar_motor(self):
        if self.disponible:
            return f"\n La motocicleta {self.marca} esta detenida"
        else: 
            return f"\n La motocicleta {self.marca} no esta disponible"
        
class Bicicleta(Vehiculo):
    def encender_motor(self):
        if not self.disponible:
            return f"\n La bicicleta {self.marca} esta en marcha"
        else: 
            return f"\n La bicicleta {self.marca} no esta disponible"
    
    def apagar_motor(self):
        if self.disponible:
            return f"\n La bicicleta {self.marca} esta detenida"
        else: 
            return f"\n La bicicleta {self.marca} no esta disponible"
        

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.coleccion_vechiculos = []

    def validar_disponibilidad(self, vehiculo):
        if vehiculo.disponible:
            print(f"\n El vehiculo {vehiculo.marca} esta disponible")
        else:
            print(f"\n El vehiculo {vehiculo.marca} NO esta disponible")

    def comprar(self, vehiculo: Vehiculo):
            if vehiculo.disponible:
                self.coleccion_vechiculos.append(vehiculo)
                vehiculo.disponible = False

class Consecionario:
    def __init__(self):
        self.clientes = []
        self.vehiculos = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"\n + El cliente {cliente.nombre} fue creado exitosamente")

    def registrar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"\n + El vehiculo {vehiculo.marca} fue creado exitosamente")

    def vender_vehiculo(self, vehiculo, cliente):
        if vehiculo in self.vehiculos:
            if vehiculo.disponible == True:
                cliente.comprar(vehiculo)
                self.vehiculos.remove(vehiculo)
                print(f"\n El vehiculo {vehiculo.marca} ha sido vendido")
            else:
                print(f"\n El vehiculo {vehiculo.marca} ya no esta disponible")
        else: 
            print(f"\n -> Este vehiculo {vehiculo.marca} ya no se encuentra disponible")

    def listar_vehiculos(self):
        print("\n --> Lista de vehiculos disponibles en el consecionario: ")
        for vehiculo in self.vehiculos:
            if vehiculo.disponible == True:
                print(f"| Marca: {vehiculo.marca} |  Color: {vehiculo.color} |  Precio: $ {vehiculo.precio} | ")


# Instancias vehiculos
camion = Camion("Foton", "azul", 200000)
moto = Motocicleta("Huskvarna", "Blanco", 50000)
bici = Bicicleta("GW", "Azul-Verde", 200)

# cliente customer
cliente1 = Cliente("Cristian")
cliente2 = Cliente("Maria")

# Consesionario DealerShip
conse = Consecionario()
conse.registrar_cliente(cliente1)
conse.registrar_cliente(cliente2)

conse.registrar_vehiculo(camion)
conse.registrar_vehiculo(moto)
conse.registrar_vehiculo(bici)

# Listar Vehiculos
conse.listar_vehiculos()

# Consultar disponibilidad
cliente1.validar_disponibilidad(camion)

# Cliente compra vehiculo
conse.vender_vehiculo(camion, cliente1)




