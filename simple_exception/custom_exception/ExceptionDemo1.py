import CheckAgeFromInput
age = 90

try:
    CheckAgeFromInput.Person.checkAge(age)
    print("Pass")
except CheckAgeFromInput.tooYoungAgeException as err:
    print("too young!")
    print("Cause by: ", str(err))
except CheckAgeFromInput.tooOldAgeException as err:
    print("too old!")
    print("Cause by: ", str(err))
except:
    print("Other exception")
    raise


