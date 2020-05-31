# list = expression for item in iterable if condition

# solution 1:
cubes = []
for i in range(1, 5):
    cubes.append(i**3)
print(cubes)

# solution 2:
list = [x**3 for x in range(1, 5)]
print(list)