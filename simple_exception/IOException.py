try:
    f = open("file.txt", "r")
    # f.write("Executing....")
except FileNotFoundError:
    print("Create a file before reading from file")
else:
    a = 1
    print("value: ", a)
    f.close()

finally:
    print("finally")

