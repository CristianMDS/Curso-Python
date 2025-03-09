
""" variable global """

y = 5

def local_function():
    """ variable local """
    x = 10 
    print(f'x: {x}')

local_function()
print(f'y: {y}') # 5, porque y es una variable global