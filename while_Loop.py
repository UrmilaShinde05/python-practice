"""count down from 10 to 1 with while. Then keep adding numbers the user types until they enter 0, 
and print the total. Then stop the loop when the user types q, using break."""

i = 10

'''while i >= 1:
    print(i)
    i -= 1

total = 0

while True:
     text = input("Enter a number (0 to stop):")
     if text == "q":
         break 
     number = int(text)
     
     if number ==0:
         break
     total += number

print("Total: ", total)'''

def addToList(a):
    a += [10]

b = [10, 20, 30, 40]
addToList(b)
print(len(b))

#_______________________________________________________

'''a = ['Python', 'Java', 'C++', 'Go']
b = a
print(b)
c = a[:]
print(c)
b[0] = 'Code'
print(b)
c[1] = 'Quiz'
print(c)
count = 0

for x in (a, b, c):
    if x[0] == 'Code':
        count += 1

    if x[1] == 'Quiz':
        count += 10

print(count)
print(a)
'''
#_______________________________________________________________________________________

def square_list(x, li=[]):
    for i in range(x):
        li.append(i * i)
    print(li)

square_list(3, [3, 2, 1])

#_______________________________________________________________________________________

"""Ask the user for a number. Using a while loop, count down from that number to 1, then print "Liftoff!"""

'''num = int(input("Enter a num:"))

while num >= 1:
    print(num)
    num -= 1

print("Liftoff!")'''
#________________________________________________________________________________________

#Keep asking the user for numbers. Stop when they type 0, 
# then print the total of all the numbers they entered.

'''total = 0

input_num = int(input("Enter a num :"))

while input_num!= 0:
    
    total = total + input_num
    input_num = int(input("Enter a num :"))
print("Total : ", total)'''

#_________________________________________________________________________________________

"""Store a secret number, say secret = 7. Keep asking the user to guess it:

If the guess is too low, print "Too low!"
If the guess is too high, print "Too high!"
If the guess is right, print "Correct! You took X tries." and stop."""

Secret_Num = 7
Guess_Num = int(input("Guess the Secret Num:"))

tries = 1

while Guess_Num != Secret_Num:
    if Guess_Num < Secret_Num:
        print("Too low!")

    elif Guess_Num > Secret_Num:
        print("Too high!")

    tries += 1

    Guess_Num = int(input("Guess the Secret Num:"))

print("Correct! You took", tries, "tries.")