listvalues = [23, 36, 13, 8, 678, 65, 658]

# Solution 1:
result = list(filter(lambda x: x % 2 == 0, listvalues))
print(result)


# Solution 2:
def takeOddValues(list):
    newList = []
    for i in list:
        if i % 2 == 0:
            newList.append(i)
    return newList


print(takeOddValues(listvalues))
