"""Santa Claus 🎅 ha recibido una lista de números mágicos que representan regalos 🎁, pero algunos de ellos están 
duplicados y deben ser eliminados para evitar confusiones. Además, los regalos deben ser ordenados en orden ascendente 
antes de entregárselos a los elfos.

Tu tarea es escribir una función que reciba una lista de números enteros (que pueden incluir duplicados) y devuelva una 
nueva lista sin duplicados, ordenada en orden ascendente."""

class Duplicados:
    def __init__(self):
        self.gifts_list = []

    def prepare_gifts(self, gifts):
        self.gifts_list = gifts

        if len(self.gifts_list) != 0:
            self.gifts_list = sorted(self.gifts_list) 
        else:
            return []

        for elemento in self.gifts_list:
            count = 0
            numero_repetido = (self.gifts_list.count(elemento) - 1)
            while count < numero_repetido:
                self.gifts_list.remove(elemento)
                count +=1

        return self.gifts_list
    
gifts = []


