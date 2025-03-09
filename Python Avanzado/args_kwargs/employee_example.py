import json
class Employee:
    def __init__(self, name: str, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs

    def show_employee(self):
        print(f"Employee: {self.name}")
        print(f"Skills: {self.skills}")
        print(f"Details: {self.details}")

skills = {
    "Lenguajes": {
        'Python', 'Java', 'JavaScript', 'PHP'
    },
    "SGDB": {
        'MySQL', 'SQL Server', 'PostgreSQL', 'SQLite'
    },
    "Cloud": {
        'AWS'
    }
}

employee = Employee('Cristian', skills, education='Uniminuto / Platzi', age=25, city='Bogota')
employee.show_employee()