def outer_function():
    x = 'encapsulado (outer)'

    # inner function
    def inner_function():
        nonlocal x
        x = 'modficado'
        print('inner:', x)

    inner_function()
    print('outer:', x)

outer_function()