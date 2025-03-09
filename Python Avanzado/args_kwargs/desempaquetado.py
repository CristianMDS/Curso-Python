# Desempaquetado de args

def add_numbers(a, b, c):
    return a + b + c


values = (8,9,5)
print(add_numbers(*values))

# Desempaquetado de kwargs
def show_kwarg(name, age):
    print(f"name: {name} - age: {age}")

kwargs = {"name": "cristian", "age": 25}
show_kwarg(**kwargs)