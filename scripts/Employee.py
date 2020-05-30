class Salary:

    def calculate_total_salary(self, basic, bonus):
        return float(basic) * 12 + float(bonus) * 5


class Employee(Salary):

    def __init__(self, employeeId=None, name=None, basicSalary=None, bonus=None):
        if employeeId is None:
            self.default_constructor()
        else:
            self.copy_constructor(employeeId, name, basicSalary, bonus)

    def default_constructor(self):
        pass

    def copy_constructor(self, employeeId, name, basicSalary, bonus):
        self.employeeId = employeeId
        self.name = name
        self.basicSalary = basicSalary
        self.bonus = bonus

    def to_json(self):
        return self.__dict__
