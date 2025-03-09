class state_account:
    def __init__(self, name: str, amount: float):
        self.name = name
        self._amount = amount
        pass

    @property
    def show_amount(self) -> float:
        return self._amount
    
    @show_amount.setter
    def show_amount(self, new_amount: float) -> (float|str):
        try:
            if new_amount < 0:
                raise ValueError('El monto de tu cuenta no puede ser negativo')
            self._amount = new_amount
            return new_amount
        except ValueError as e:
            return f"Error: {e}"
        
    @show_amount.deleter
    def show_amount(self) -> str:
        des = input("Tu cuenta va a ser eliminada es esto correcto [Y/N]: ")
        if des in ('Y', 'y'):
            print("Cuenta eliminada")
            del self.name, self._amount
        elif des in ('N', 'n'):
            print("proceso cancelado")
    
obj = state_account('Cristian', 800)
print(obj.show_amount)
obj.show_amount = 1500
print(obj.show_amount)
del obj.show_amount
