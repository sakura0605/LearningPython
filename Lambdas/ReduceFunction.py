
from functools import reduce
import operator
import itertools

# Using Reduce function to find sum of elements in list
#1
listvalues = [10, 20, 10]
result = reduce(lambda x, y: x+y, listvalues)
print(result)

#2
result = reduce(operator.add, listvalues)
print(result)

#3
result = reduce(operator.mul, listvalues)
print(result)

#4
result = list(itertools.accumulate(listvalues, lambda x, y: x + y))
print(result)

# using reduce to find max value
result = reduce(lambda x, y: x if x >= y else y, listvalues)
print(result)
