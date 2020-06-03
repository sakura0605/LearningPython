class Salary:

    def calculate_total_salary(self, basic, bonus):
        return float(basic) * 12 + float(bonus) * 5


# Solution 1:
class Employee(Salary):

    def __init__(self, employeeId=None, name=None, basicSalary=None, bonus=None, salary=None):
        if employeeId is not None:
            self.employeeId = employeeId
        if name is not None:
            self.name = name
        if basicSalary is not None:
            self.basicSalary = basicSalary
        if bonus is not None:
            self.bonus = bonus
        if salary is not None:
            self.salary = salary

    def to_json(self):
        return self.__dict__
