count = 1
while count <=10:
    print(count)
    count += 1

count = 1
while True:
    print(count)
    count += 1
    if not(count<=3):
        break

a = int(input("Enter a number: "))
count = 1
while count <= 10:
    print(f"{count} \t x {a:5} \t = \t {count*a}")
    count += 1

count = 1
while True:
    print(f"{count} \t x \t {a:5} \t = \t {count*a}") 
    count += 1
    if (count >=10):
        break