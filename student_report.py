"""Week 1 check, part 1 (about 1 hour)

Retype one example each of input(), print(), arithmetic, and comparison operators.
Create student_report.py. Ask for the student’s name, then ask for three marks, converting each with float().
Print the total and the average."""

name = input("Enter your name: ")
mark1 = float(input("Enter your first mark: "))
mark2 = float(input("Enter your second mark: "))
mark3 = float(input("Enter your third mark: "))

total = mark1 + mark2 + mark3
average = total / 3

print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")

# Grade the student based on the average mark using if, elif, and else statements. Print the grade.

if average >=80:
    print("Grade: A")

elif average >= 60:
    print("Grade: B")

elif average >= 40:
    print("Grade: C")

else:
    print(" Grade: F")

if average >= 40:
    print("Pass")
else:
    print("Fail")