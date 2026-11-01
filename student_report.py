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