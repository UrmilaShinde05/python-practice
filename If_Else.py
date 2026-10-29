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

'''age = float(input("Enter the Child Age :"))

if age < 13:
    print("child")

elif age <= 19:
    print("teen")

else:
    print("adult")'''

#____________________________________________________________

#Write a block that takes two numbers `a` and `b` and prints `"a is bigger"`, `"b is bigger"`, or `"equal"`

'''a = float(input("Enter the first number :"))
b = float(input("Enter the second number :"))

if a > b:
    print("a is bigger")
elif b > a:
    print("b is bigger")
else:
    print("equal")'''

#What is the difference between `if`, `elif`, and `else`? When would you use each one?

# `if` is used to check the first condition.
# `elif` is used to check additional conditions if the previous `if` or `elif` conditions are not met.
# `else` is used to execute a block of code if none of the previous conditions are met.

#example:

n = 12
if n > 5:
    print("A")
if n > 10:
    print("B")

# example2: for Elif
n = 12
if n > 5:
    print("A")
elif n > 10:
    print("B")
else:
    print("C")

