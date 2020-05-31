a = [1, 3, 2, 4, 5]
b = [2, 3, 7, 4, 5]

# solution 1:
result = []
for x in range(len(a)):
    result.append(a[x] * b[x])
print(result)


# solution 2:
result = [a[x] * b[x] for x in range(len(a))]
print(result)