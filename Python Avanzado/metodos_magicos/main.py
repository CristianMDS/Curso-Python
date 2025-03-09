
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        if b == 0:
            raise ValueError('No se puede dividir por 0')
        else:
            return a / b
    except ValueError as e:
        print(f"Error: {e}")
    

if __name__ == "__main__":
    print("operaciones")
    ans_1 = add(5, 7)
    print(f"Suma: {ans_1}")
    ans_2 = sub(5, 10)
    print(f"Resta: {ans_2}")
    ans_3 = mul(2, 5)
    print(f"Suma: {ans_3}")
    ans_4 = div(5, 0)
    print(f"division: {ans_4}")
