#If-Else Conditions satement

# Ternary Operator
'''age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)'''

# Match Case statement
number = 2

'''match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")'''

# Write an `if`, `elif`, `else` block that takes a number `n` and prints `"even"` if it's even, or `"odd"` if it's odd. Use `%`.

'''x = int(input("Enter the Num :"))
if x % 2 == 0:
    print("Given no. is Even")
else:
    print("Given no. is odd")'''
#Write a block that takes an age and prints `"child"` if under 13, `"teen"` if from 13 to 19, and `"adult"` for 20 or more.

age = float(input("Enter the Child Age :"))

if age < 13:
    print("child")

elif age <= 19:
    print("teen")

else:
    print("adult")

