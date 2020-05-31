# 1. assign function to variable
def printA():
    print("hello")

a = printA
a() # to call the function printA()

# 2. function inside function
def display(name):
    def message():
        return "Hello "
    return message() + name

print(display("Hoa"))

# 3. return function
def display_1():
    def message():
        return "Hello_1"
    return message

fun = display_1()
print(fun())
