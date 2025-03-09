import pprint

class Libro:
    def __init__(self, titulo, autor, genero, codigo):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = True

    def prestamo(self):
        if self.disponible == True:
            self.disponible = False
            print(f"\n - El libro {self.titulo} ha sido prestado")
        else:
            print(f"\n - El libro {self.titulo} no esta disponible")
        
    def regresarLibro(self):
        self.disponible = True
        print(f"\n - El libro {self.titulo} ya esta disponible")

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_Id = user_id
        self.libros_Prestados = []

    def prestar_Libro(self, libro):
        if libro.disponible == True:
            libro.disponible = False
            self.libros_Prestados.append(libro)
            print(f"El libro {libro.titulo} del autor {libro.autor}, fue prestado al usuario {self.nombre} cod. {self.user_Id}")
        else:
            print(f" - El libro {libro.titulo} no esta disponible -")

    def devolver_Libro(self, libro):
        if libro in self.libros_Prestados:
            libro.regresarLibro()
            self.libros_Prestados.remove(libro)
        else:
            print(f"El libro {libro.titulo} No se encuntra dentro de la lista de prestamos")

    def revisar_Libros(self):
        print(" -> Los libros que tienes que devolver o leer son: ")
        for librox in self.libros_Prestados:
            print(librox.titulo)

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []

    def añadir_Libros(self,libro):
        self.libros.append(libro)
        print(f"\n + El libro {libro.titulo} ha sido agregado")

    def registrar_Usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"\n - El usuario {usuario.nombre} ha sido registrado")

    def libros_Disponibles(self):
        print(f"\n = Los libros disponibles son: ")
        for libro in self.libros:
            if libro.disponible:
                print(f"| titulo -> {libro.titulo} - autor -> {libro.autor} | \n")
    


# Libros
libro1 = Libro('Harry Potter y la piedra filosofal', 'JK Rowling', 'Fantasia', '001')
libro2 = Libro('La biblia de los caidos', 'Fernando algo', 'Fantasia', '002')
libro3 = Libro('Historias oscuras', 'Edgar Alan Poe', 'Terror', '003')

# usuarios
user1 = Usuario('Cristian', '001')
user2 = Usuario('David', '002')

# biblioteca
virgilioBarco = Biblioteca()
virgilioBarco.añadir_Libros(libro1)
virgilioBarco.añadir_Libros(libro2)
virgilioBarco.añadir_Libros(libro3)
virgilioBarco.registrar_Usuario(user1)
virgilioBarco.registrar_Usuario(user2)

# Mostrar libros
virgilioBarco.libros_Disponibles()

# Prestar libros
user1.prestar_Libro(libro1)

# Trato de prestar el mismo libro
user2.prestar_Libro(libro1) # funciona bien, todo es muy secuncial razon por la cual si consulto el usuario 
                            # que tiene el libro me muestra el user2 que es quien ejecuta la accion mas no el 
                            # que lo tiene.

# Mostrar libros
virgilioBarco.libros_Disponibles()

# Le presto al segundo otro libro
user2.prestar_Libro(libro2)

# Mostrar libros
virgilioBarco.libros_Disponibles()

user1.revisar_Libros()

# Ahora regresamos el libro del primero
# user1.devolver_Libro('Harry Potter y la pieda filosofal')  <- Aqui esta mal estoy buscando el libro por titulo
                                                            # pero el argumento solicita un objeto ( libro1 , libro2 , etc)
                                                            # Por esa razon no pasa el argumento al ejecutar la funcion.
                                                        
# Ahora si regresamos el libro 
user1.devolver_Libro(libro1)

# Obviamente el libro3 no lo tiene el user2
user2.devolver_Libro(libro3)

# devolvemos el ultimo libro
user2.devolver_Libro(libro2)



