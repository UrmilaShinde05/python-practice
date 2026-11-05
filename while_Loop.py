"""count down from 10 to 1 with while. Then keep adding numbers the user types until they enter 0, 
and print the total. Then stop the loop when the user types q, using break."""

i = 10

while i >= 1:
    print(i)
    i -= 1

total = 0

while True:
    
   text = int(input("Enter a number (0 to stop):"))

   if text == "q":
          break 
   number = int(text)
   
   if number ==0:
       break
   total += number

print("Total: ", total)
