'''file = open("notes.txt", "r")
contents = file.read()
print(contents)
file.close()'''

#____________________________________________________________________________________________

"""with open("notes.txt") as file:
    lines = file.readlines()
for line in lines:
    print(line.strip())"""

#_______________________________________________________________________________________________

"""with open("notes.txt", "w") as file:

    file.write("Hello World!! \n")
    file.write("Welcome to Python. \n")

with open("notes.txt", "r") as file:
    print(file.read())

with open("notes.txt", "a") as file:
    file.write("New Entry is added \n")

with open("notes.txt", "r") as file:
    print(file.read())"""

#______________________________________________________________________________________________

tasks = ["Buy Grocessary \n", "Walk the Dog \n", "Finish Homwork \n"]

with open("text.txt" , "w") as file:
    file.writelines(tasks)

with open("text.txt","r") as file:
    print(file.read())

    

