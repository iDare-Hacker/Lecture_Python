#1. Write a program to print all even numbers between 1 and 50 using range().
for i in range(2, 51, 2):
    print(i)

#2. Write a program to print a multiplication table (1 to 10) for a number using a for loop.
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#3. Write a program to print a number pyramid: 1 / 1 2 / 1 2 3 / 1 2 3 4.
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to the next line after each row


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")
    print(fruit[0:3], end=" : ")
    for cr in fruit:
        print(cr.upper(), end=".")
    print()
