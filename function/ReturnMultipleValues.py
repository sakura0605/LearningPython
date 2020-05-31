def calc(a, b):
    x = a * b
    y = a - b
    z = a + b
    t = a / b
    return x, y, z, t

result = calc(10, 2)
print(result)
for i in result:
    print(i)