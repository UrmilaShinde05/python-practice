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