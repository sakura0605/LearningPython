class Student:

    def __init__(self, fullname, age, gpa):
        self.fullname = fullname
        self.age = age
        self.gpa = gpa

    def __init__(self):
        pass

    def to_json(self):
        return self.__dict__

    def from_json(self, str_student):
        self.__dict__ = str_student

    def toString(self):
        return self.fullname + "\t" + str(self.age) + "\t" + str(self.gpa)
