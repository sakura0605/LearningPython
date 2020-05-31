# 1 len(a)==len(b) find common numbers
a = [1, 2, 3, 4, 5, 6]
b = [1, 0, 6, 4, 8, 6]

result = [i for i in a if i in b]
print(result)

# 2 len(a) !=len(b) find different number in a not in b
a = [1, 2, 3, 4, 5]
b = [1, 0, 6, 4, 8, 6]

result = []
for i in a:
    if i not in b:
        result.append(i)
print(result)

