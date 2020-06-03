# Factory methods are those methods which return a class object (like constructor) for different use cases
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Create factory method using class method
    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    @classmethod
    def person_Have_Level(cls, name, age):
        return cls(name, age)

    def display(self):
        print("name: ", self.name, "\tage: ", self.age)


# person = Person("Adam", 19)
# person.display()
#
person1 = Person.fromBirthYear("Ann", 1996)
person1.display()

person2 = Person.person_Have_Level("Mike", 17)
person2.display()
