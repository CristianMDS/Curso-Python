def check_rol(required_rol):
    def decorator(func):
        def wrapped(employee):
            if employee.get('rol') == required_rol:
                return func(employee)
            else:
                print("Acceso denegado")
        return wrapped
    return decorator

def log_action(func):
    def wrapped(employee):
        print(f"Registrado la accion del empleado {employee["name"]}")
        return func(employee)
    return wrapped
        

@check_rol('admin')
@log_action
def delete_employee(employee):
    print(f"El empleado {employee['name']} ha sido eliminado")


lista = {
    "Cristian": {"rol": "admin", "job_title": "Senior Developer"},
    "David": {"rol": "employee", "job_title": "Mid Developer"},
    "Mora": {"rol": "employee", "job_title": "Mid Developer"},
    "Saenz": {"rol": "employee", "job_title": "Junior Developer"}
}  

delete_employee(lista)