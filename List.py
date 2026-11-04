'''electricity = [4, 6, 8, 12, 5, 15, 7]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]'''


#Palindrom no.

num = int(input ("Enter Palindrome Num: "))

if str(num) == str(num)[::-1]:
    print(f"{num} is palindrom num")
else:
    print(f"{num} is not palindrom num")