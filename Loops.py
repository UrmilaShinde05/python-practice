#for loops and range(). Type each example your self. Start with for i in range(5): print(i), and predict the output before you run it. Then try range(2, 10, 2).
"""print numbers 1 to 10, print the even numbers from 1 to 20, 
and print the multiplication table for a number the user enters."""

"""for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)"""

#____________________________________________________________________________________________________________

'''text = "Python"

for char in reversed(text):
    print(char)'''
#____________________________________________________________________________________________________________
'''d = {0, 1, 2}
for x in d:
    print(x)'''
#____________________________________________________________________________________________________________

'''x = 'abcd'
for i in range(len(x)):  
    print(i, end= " ")'''
#__________________________________________________________________________________________________________

numbers = [1, 2, 3, 4, 5]
for i, num in enumerate(numbers):
   if i % 2 == 0:
       continue
   print(num, end=' ')
#__________________________________________________________________________________________________________

'''for i in range(5):
    print(i)

for x in range(2,10,2):
    print(x)

for y in range(10,0,-1):
    print(y)

for z in range(1,11,3):
    print(z)
'''
"""Ask for the names of 5 employees.
Accept each employee's salary.
Store employee names in a list.
Store salaries in another list.
Display all employee names and salaries.
Calculate total salary expenditure.
Find the highest salary.Find the lowest salary."""

'''Employee_Name = []
Employee_Salary = []

for i in range (5):
    Employee_Name.append(input ("Enter employee name: "))
    Employee_Salary.append(float(input("Enter employee salary: ")))

print(Employee_Name)
print(Employee_Salary)

total_salary = sum(Employee_Salary)
highest_salary = max(Employee_Salary)
lowest_salary = min(Employee_Salary)

print(f"Total salary expenditure: {total_salary}")
print(f"Highest salary: {highest_salary}")
print(f"Lowest salary: {lowest_salary}")'''

'''Ask how many employees you want to enter.
Accept employee name.
Accept department name.
Accept employee salary.
Store employee information.
Display all employee records.
Calculate total salary expenditure.
Calculate average salary.

O/p : employee = {
    "name": "Rahul",
    "department": "IT",
    "salary": 50000
}'''

'''Num_Employees = int(input("Enter the number of employees you want to enter: "))
Employees_records = {}

for i in range(Num_Employees):
    name = input("Enter employee name: ")
    department = input("Enter department name: ")
    salary = float(input("Enter employee salary: "))

    Employees_records[name] = {
        "Name": name,
        "Department": department,
        "Salary": salary
    }

Employee_names = list(Employees_records.keys(): Employees_records.values())
print("\n_________Employee Details_________")

for'''

#_____________________________________________________________________________________________________________
# Employee Salary Management System

'''employees = []

num_employees = int(input("How many employees do you want to enter? "))

# Step 1: Collect employee information

for i in range(num_employees):

    print(f"\nEnter details of Employee {i + 1}")

    name = input("Employee Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    employee = {
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)


# Step 2: Display employee records

print("\n======= EMPLOYEE RECORDS =======")

for employee in employees:

    print(f"Name: {employee['name']}")
    print(f"Department: {employee['department']}")
    print(f"Salary: Rs. {employee['salary']:,.2f}")
    print("-------------------------------")


# Step 3: Calculate total salary

total_salary = 0

for employee in employees:
    total_salary = total_salary + employee["salary"]


# Step 4: Calculate average salary

if num_employees > 0:
    average_salary = total_salary / num_employees
else:
    average_salary = 0


# Step 5: Display salary summary

print("\n======= SALARY SUMMARY =======")

print(f"Total Salary Expenditure: Rs. {total_salary:,.2f}")
print(f"Average Salary: Rs. {average_salary:,.2f}")
print(f"Total Employees: {num_employees}")'''

#____________________________________________________________________________________________________________

"""Exercise 5: The Password Attempt System
Situation: A user has only three attempts to enter the correct password.

Your task:
- Set a password in your program.
- Ask the user to enter it.
- Allow three attempts.
- Display a success message if correct.
- Display an account locked message if all attempts fail."""

'''password = "Radha123"

attempts = 3

while attempts > 0:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Password correct. Access granted.")
        break
    else:
        attempts = attempts - 1
        if attempts > 0:
            print(f"Incorrect password. You have {attempts} attempts left.")
        else:
            print("Account locked. Too many failed attempts.")'''