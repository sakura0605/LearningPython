# if global and local variables have the same name
x = 10  # glocal variable

def calc():
    x = 5  # local variable
    print("global---", globals()['x'])  # call glocal variable
    return "local---" + str(x);


print(calc())
