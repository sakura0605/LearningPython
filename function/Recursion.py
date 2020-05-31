# factorior(n) = n * factorior(n - 1)
# factorior(0) = 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
