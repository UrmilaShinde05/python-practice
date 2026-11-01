"""Week 1 check, part 1 (about 1 hour)

Retype one example each of input(), print(), arithmetic, and comparison operators.
Create student_report.py. Ask for the student’s name, then ask for three marks, converting each with float().
Print the total and the average."""

x = input("Enter your name: ")
y = float(input("Enter your first mark: "))
z = float(input ("Enter your second mark: "))
w = float(input("Enter your third mark: "))

total = y + z + w
average = total / 3

print(f"Student: {x}")
print(f"Total: {total}")
print(f"Average: {average}")

# Grade the student based on the average mark using if, elif, and else statements. Print the grade.

x = input ("enter your name:")

if average >=80:
    print("Grade: A")

elif average >= 60 and average < 79:
    print("Grade: B")

elif average >=40 and average < 59:
    print("Grade: C")

elif average > 40:
    print(" Grade: F")

else:
    print("Fail")