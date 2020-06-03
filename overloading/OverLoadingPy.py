# Reference:
# https://www.codementor.io/@arpitbhayani/overload-functions-in-python-13e32ahzqt


# 1. overloading Built-in Functions
# To change the default behavior of Python's build-in functions.
#  Only have to define the corresponding special method in our class
#  from typing import overload


class Purchase:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        return len(self.basket)


purchase = Purchase(['a', 'b', 'c'], "Python")

# The result depends on len() function in the Purchase class
print(len(purchase))


# 2. overloading User-Defined Functions:
# To write function logic in such a way that depending upon the parameters passed,
# a different piece of code executes inside the function.
# for example: constructor

class Student:
    def __init__(self, name=None, age=None, level=None):
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if level is not None:
            self.level = level
        else:
            pass

    def display_1(self):
        print(self.name, "--", self.age, "--", self.level)

    def display_2(self):
        print(self.name, "--", self.age, "--", self.salary)


st_1 = Student("Hoang", 23, None)
st_1.__setattr__("salary", 4234.354)
st_1.display_2()

st_2 = Student("Jack", 13, "Level 6")
st_2.display_1()


# 3. overloading User-Defined Functions:
# If no argument then it returns 0
# If have one argument then it returns the square of the value(computing the area of a square)
# If have two arguments then it returns the product of the two values(computing the area of a rectangle)


class Compute:
    def area(self, x=None, y=None):
        if x is not None and y is not None:
            return x * y
        elif x is not None:
            return x * x
        else:
            return 0;


obj = Compute()
print("Area value: ", obj.area())
print("Area value: ", obj.area(3))
print("Area value: ", obj.area(2, 5))
