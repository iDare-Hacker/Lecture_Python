#1. Write a program that prints numbers from 1 to 50 but stops as soon as it finds a number divisible by both 7 and 5.
for i in range(1, 51):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
        break
    print(i)

#2. Write a program that prints all numbers from 1 to 30, skipping multiples of 3, using continue.
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)