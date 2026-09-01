#1
year = int(input("Enter a year: ")) 
 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
    print(f"{year} is a Leap Year") 
else: 
    print(f"{year} is NOT a Leap Year") 


#2
a = int(input("Enter a number: "))
count = 1
while count <= 10:
    print(f"{count} \t x {a:5} \t = \t {count*a}")
    count += 1

