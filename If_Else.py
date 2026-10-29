#If-Else Conditions satement

# Ternary Operator
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

# Match Case statement
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
        