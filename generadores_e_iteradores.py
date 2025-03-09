list = [1,2,3,4,5]

new_iter = iter(list)
x = 0
while x < len(list):
    print(next(new_iter))
    x += 1