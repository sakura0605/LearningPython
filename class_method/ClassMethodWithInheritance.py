# Reference:
# 1. https://radek.io/2011/07/21/static-variables-and-methods-in-python/#:~:text=Static%20means%2C%20that%20the%20member,value%20in%20all%20other%20instances.

from datetime import date

# 1.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFatherAge(name, fatherYear, diff):
        return Person(name, date.today().year - fatherYear - diff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print("name: ", self.name, "----age: ", self.age)


class Man(Person):
    gender = "Male"

man_1 = Man.fromBirthYear("Hoa", 1996)
man_1.display()
# Instance of child
print(isinstance(man_1, Man))

man_2 = Man.fromFatherAge("Hien", 1988, 20)
man_2.display()
# Instance of parent
print(isinstance(man_2, Person))

# 2.


class Person:

    def calculate_salary(self, basic, bonus):
        return float(basic) + float(bonus)


class Employee(Person):
    def __init__(self, name=None, age=None, basic=None, bonus=None, salary=None):
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if basic is not None:
            self.basic = basic
        if None != bonus:
            self.bonus = bonus
        if None != salary:
            self.salary = salary


    def display(self):
        print("name: ", self.name, "\tage: ", self.age, "\tsalary: ", self.salary)


e = Employee("Hoa", 18, 1000.5, 200)
basic = e.basic
bonus = e.bonus
salary = e.calculate_salary(basic, bonus)
print(salary)

e.__setattr__("salary", e.calculate_salary(float(e.basic), float(e.bonus)))
e.display()


