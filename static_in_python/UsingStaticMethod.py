# using staticmethod()
class Calculator:

    def addNumbers(a, b):
        return a + b


Calculator.addNumbers = staticmethod(Calculator.addNumbers)
print("sum: ", Calculator.addNumbers(2, 10))


# using @staticmethod
class Account:
    number = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def average(a, b):
        return (a + b) / 2

    @staticmethod
    def count():
        print("number: ", Account.number)


print("average: ", int(Account.average(10, 20)))
a = Account("", "")
a.count()
