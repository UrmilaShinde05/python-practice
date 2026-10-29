'''print("Hello, Urmila")
x = int(input("Please enter an Intergerno. :"))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")'''

# Measure some strings:

'''words = ['cat', 'window', 'defenstrate']
for x in words:
    print(x,len(x))'''

    #---------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------

## Create sample collections

users = {'Hans' : 'Active', 'Morgan' : 'Inactive', 'Shyam' : 'Active'}

#Strategy : Iterate over the copy

'''for user, status in users.copy().items():
    if status == 'Inactive':
        del users[user]

#strategy create a new collections

active_users = {}
for user, status in users.items():
    if status == 'Active':
        active_users[user]= status
        
print(active_users)'''
#________________________________________________________________________________________________________________________
#Multiple variable can assign the same values
'''a = b = c = 100
print(a, b, c) '''

#______________________________________________________________________________________________________________________

#Multiple Variable can assign the multiple value by using below

'''x, y, z = 1, 2.5, "Python"
print(x, y, z)''' 

#_________________________________________________________________________________________________________________
#Reassignment of Variable can delete from previous assigned variable

'''x = 5
y = x
x = 'Geeks'
y = "Computer"
y = x
print(x,y)'''

"""x = 1
y = x
y = y + 1
print(x)
print(y)"""

#____________________________________________________________________________________________________________

#Delete variable is used to delet from the memory

"""x = 10
del x
print(x)"""

#___________________________________________________________________________________________________________________
#print(reverse_words("hello big world"))

#___________________________________________________________________________________________________________________

#Swapping two variables
'''a, b = 5, 10
a, b = b, a
print(a, b)'''

#__________________________________________________________________________________________________________

#Counting Character in a string 

'''word = "Python"
length = len(word)
print("Length of the word:", length)'''

#_______________________________________________________________________________________________________________________
#Numeric Data Type 

'''a = 5
b = 5.0
c = 2 + 4j

print(type(a))
print(type(b))
print(type(c))'''

#_________________________________________________________________________________________________________________

## Squence Data Type Example

#String 

'''s = 'Welcome to the World'
print(s)
print(type(s))

# access string with index
print(s[0])
print(s[-1])'''

#List: Mutable collections used for multiple items in a single variable

'''a = [1, 2, 3]
print(a)

b = ["Greens", "For", "Rani", 4, 5]

#List can access through indexing

print(b[3])
print(b[-3])'''

#Tuple : Tuple are immutable collections used to stored multiple itemns in single variable 
## once Tuple created tuple can't be modified and are accessed using Indexing
#Fro single element in the tuple must be followed by ,

'''t1 = (1,)
print(type(t1))

t2 = ('Green', 'For', 'Green', 1, 2)
print(t2[3])
print(t2[-3])'''
#_____________________________________________________________________________________________________________________________

#Boolean Data Type
'''print(type(True))
print(type(False))'''

#______________________________________________________________________________________________________________

# strings are immutable 
#Error : 'str' object does not support item assignment

'''message = "Welcome to GeeksforGeeks"
message[0] = 'p'
print(message)'''

# String are immutable any modification done in string it creates a new string instead of alterning the original one

s = "aBCDEF"
s = "A" + s[1:]
print(s)

##String deletion

'''s1 = "ABC"
del s1'''

#String updating 

'''s2  = "  ABCDEF  "
s3 = "H" + s2[1:]
s4 = s2.replace("ABC" , "abc")
print (s3)
print(s4)'''

# String upper and lower method

'''print (s.upper())
print(s.lower())'''

# s2.strip() ## Remove leading spaces and trailing spaces from the sting

'''a = " I am awesome"
b = a.replace("awesome" , "funloving")
print(b)
# or 
print (a.replace("awesome" , "funloving"))'''

#Concatenating and Repeating Strings
'''s1 = "Hello"
s2 = "Supermom"
print(s1 + " " + s2)
print(s1 * 3)'''

word = ["Python" , "is" , "Easy"]
print("_".join(word))



#________________________________________________________________________________________________________

#Lists are mutable in Python. We can add or remove elements from the list. 
# In Python, mutability refers to the capability of an object to be changed or modified after its creation.


'''my_list = [1, 2, 3]
my_list.append(4)
print(my_list) 

my_list.insert(1, 5)
print(my_list) 

my_list.remove(2)
print(my_list) 

popped_element = my_list.pop(0)
print(my_list)         
print(popped_element)'''


#_____________________________________________________________________________________________________________

#Set Data Type : Set data type is mutable and its element is access by the loop only not by indexing 
#Set Data Type is unordered and Mutable used to staored unique element

'''s1 = {"a", "a", "b", "c", "b"}
print(s1)

s2 = {"Geeks", "For", "Geeks"}
for i in s2:
    print(i)'''
#_________________________________________________________________________________________________________________

#Dictionary Data Type : in this type values are used to store in Key : Value , Each key in Dictionary have unique key
#Values are accessd by [] and get() method

'''d = {1: 'Green', 2: 'For', 3: 'Green'}
print(d[1])    
print(d.get(2))'''

#Test Exmple for Dictionary

'''a = {'a': 1, 'b': 2}
b = a
a = {'c': 3}
print(b)'''

#__________________________________________________________________________________________________________________

#Arithmethic Operator

'''a = 15
b = 4

print("Addition:", a + b)  

print("Subtraction:", a - b) 

print("Multiplication:", a * b)  

print("Division:", a / b) 

print("Floor Division:", a // b)  

print("Modulus:", a % b) 

print("Exponentiation:", a ** b)'''
#______________________________________________________________________________________________________________________

#Comparison Operator

'''a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)'''

#___________________________________________________________________________________________________________________

#Logical Operators

'''a = True
b = False
print(a and b)
print(a or b)
print(not a)'''

#________________________________________________________________________________________________________

'''print("1 :", -7 // 2)
print("2 :", 2 ** 4)
print("3 :", 2 ** 3 * 2)
print("4 :", 7 // 2)
print("5 :", 7 % 3)
print("6 :", 2 ** 4)
print("7 :", 10 / 4)
print("8 :", 5 != 3)
print("9 :", 4 >= 4)
print("10 :", 3 < 2)
print("11 :", True and False)
print("12 :", True or False)
print("13 :", not True)
print("14 :", 5 > 2 and 3 > 1)
print("15 :", 2 ** 3 * 2)
print("16 :", 10 != 10.0)
print("17 :", 10 == 10.0)'''
