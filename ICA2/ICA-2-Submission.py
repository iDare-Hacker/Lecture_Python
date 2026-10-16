##################################################
# ICA2 - 4 Questions 5 Marks Each
####################################################

"""Q1. [Python Basics & Data Structures] Let names = ["Rohan", "aman", "Zoya", "bhavna"]. Sort the list using sort() and
print it. In a comment, explain why "Rohan" and "Zoya" appear before "aman" in the output. [5 Marks]"""

names = ["Rohan", "aman", "Zoya", "bhavna"]

names.sort()
print(names)

# The reason "Rohan" and "Zoya" appear before "aman" in the output is because the sort() 
# method sorts strings based on their ASCII values. Uppercase letters have lower ASCII 
# values than lowercase letters, so all uppercase names will come before any lowercase names when sorted.



"""Q2. [Strings, I/O & Operators] Accept the radius of a circle and print its area (use 3.14159) in the format "The area of
the circle with radius 5.0 cm is 78.54 sq cm", showing the area to 2 decimals. [5 Marks]
"""

radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius ** 2
print(f"The area of the circle with radius {radius} cm is {area:.2f} sq cm")



"""Q3. [Control Flow & Loops] Using a for loop, print the sum of the first n natural numbers and the sum of their squares,
where n is entered by the user. [5 Marks]
"""

n = int(input("Enter the value of n: "))
sum_n = 0
sum_squares = 0

for i in range(1, n + 1):
    sum_n += i
    sum_squares += i ** 2

print(f"The sum of the first {n} natural numbers is {sum_n}")
print(f"The sum of the squares of the first {n} natural numbers is {sum_squares}")



"""Q4. [Functions] Write a function min_max(numbers) that returns BOTH the smallest and the largest value (without
using min() and max()). Call it and unpack the two returned values into separate variables. [5 Marks]"""

def min_max(numbers):
    if not numbers:
        return None, None
    min_val = max_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_value, max_value = min_max(numbers)
print(f"Min: {min_value}, Max: {max_value}")