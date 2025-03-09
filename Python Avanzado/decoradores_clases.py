class country:
    city: str

    def __init__(self, ciudad: str):
        self._city = ciudad

    @property
    def show_city(self) -> str:
        return f"Esta viviendo en la ciudad: {self._city}"
    
    # @property
    # def city(self) -> str:
    #     return self._city

    @show_city.setter
    def change_city(self, new_city: str):
        if not isinstance(new_city, str):
            raise TypeError("La ciudad debe ser de tipo String")
        
        self._city = new_city
    

city = country("Bogota")
print(city.show_city)
city.change_city = "Medellin" # Como es un setter no es necesario usar los () parentesis, 
                                # basta con la igualdad
print(city.show_city)