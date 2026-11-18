'''electricity = [4, 6, 8, 12, 5, 15, 7]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]'''


#Palindrom no.
"""
num = int(input ("Enter Palindrome Num: "))

if str(num) == str(num)[::-1]:
    print(f"{num} is palindrom num")
else:
    print(f"{num} is not palindrom num")"""
#______________________________________________________________________________

#List index returns the Position of occurrence of the element in the list. 
# If the element is not found, it raises a ValueError.

li = list(range(100, 110))
print(li.index(105))

#_____________________________________________________________________________________

a = ['python', 'coding', '@', 'apple', 'banana', 'orange']
print(a[0:6:2])

