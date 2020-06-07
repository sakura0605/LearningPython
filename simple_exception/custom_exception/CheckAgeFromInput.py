class ageException(Exception):
    def __init__(self, mgs, age):
        super().__init__(mgs)
        self.age = age


class tooYoungAgeException(ageException):
    def __init__(self, mgs, age):
        super().__init__(mgs, age)


class tooOldAgeException(ageException):
    def __init__(self, mgs, age):
        super().__init__(mgs, age)


def checkAge(age):
    if age < 18:
        raise tooYoungAgeException("Age "+str(age)+" is too young! ", age)
    elif age > 40:
        raise tooOldAgeException("Age "+str(age)+" is too old! ", age)
    else:
        print("Age ", str(age), "is OK!")


class Person:
    @staticmethod
    def checkAge(age):
        if age < 18:
            raise tooYoungAgeException("Age " + str(age) + " is too young! ", age)
        elif age > 40:
            raise tooOldAgeException("Age " + str(age) + " is too old! ", age)
        else:
            print("Age ", str(age), "is OK!")