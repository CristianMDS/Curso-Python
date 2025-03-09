# super() es utilizado para heredar las caracteristicas de un metodo de la clase padre

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def accelerate(self):
        print(f"Hi, my car is {self.color} and her sound is rrun run")

class Lambo(Car):
    def __init__(self, color, brand, price):
        super().__init__(color, brand)
        self.price = price

    def __str__(self):
        return f"\n color: {self.color} - brand: {self.brand}"

    def __repr__(self):
        return f"\n Car(brand = {self.brand}, color = {self.color}, Price = {self.price})"

    def accelerate(self):
        super().accelerate()
        print(f"and her brand is {self.brand}, the price of this car is {self.price}")
    

lambo = Lambo("blue", "Lamborghini", 1500000)
print(lambo, "\n") # representacion de forma escrita sobre nuestro objeto
print(repr(lambo), "\n") # representacion de formar estructural de nuestro objeto
lambo.accelerate()
    