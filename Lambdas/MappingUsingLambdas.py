listvalues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(map(lambda x: x * 2, listvalues))
print(result)


def multiply(x):
    return x * x


def add(x):
    return x + x


def subtraction(x):
    return x - 1

funcs = [multiply, subtraction]

for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

