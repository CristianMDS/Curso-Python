"""
reto:
    implementar una clase 'CuentaBancaria' con un metodo protegido para registrar las transacciones internamente
    1. El metodo protegido (_actualizar_saldo) solo debe ser utilizado dentro de la clase y sus subclases
    2. El metodo privado (__registrar_transaccion) debe  ser completamente interno y no accesible fuera de la clase
"""
import json
from datetime import datetime
class Bank_Account:
    def __init__(self, account: dict):
        self.account = account

    def __record_transaction(self, code_account: int, amount: int):
        date = str(datetime.now())
        self.account[code_account]["history_account"].update({
            date: {
                "state": "Update amount in your account",
                "amount": amount
            },
        })

    def _update_amount(self, code_account: int, amount: float):
        self.account[code_account]["amount"] = amount
        self.__record_transaction(code_account, amount)

    def show_state_account(self, code_account: int):
        print(json.dumps(self.account[code_account], indent=4))


account = {
    # code_account
    123476: { 
        "propietario": "cristian M",
        "amount": 1000,
        "history_account": {}
    }
}

obj = Bank_Account(account)
obj._update_amount(123476, 2000)
obj.show_state_account(123476)
