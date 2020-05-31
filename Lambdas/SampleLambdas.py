# lambda is anonymous function
'''def cube(n):
    return n ** 3


print(cube(2))'''

f = lambda n: n**3
print(f(2))


# Yes/No with odd/even values
f = lambda x: "Yes" if x % 2 == 0 else "No"
print(f(20))
print(f(1))


# Calculate sum of two numbers
f = lambda x, y: x + y
print(f(20, 10))