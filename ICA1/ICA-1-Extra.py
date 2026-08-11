"""Q1. Two sets, A and B, contain roll numbers of students who took a Python test and an Excel test respectively. Write a
program to display the union, intersection, and the students who appeared for ONLY the Python test. [10 Marks]"""

set_A = {101, 102, 103, 104, 105} 
set_B = {104, 105, 106, 107} 

set_union = set_A.union(set_B)
print("Union of sets A and B:", set_union)
set_intersection = set_A.intersection(set_B)
print("Intersection of sets A and B:", set_intersection)
set_only_python = set_A.difference(set_B)
print("Students who appeared for ONLY the Python test:", set_only_python)


"""Q2. An electricity board charges as follows: first 100 units @ Rs 3/unit, next 100 units @ Rs 4.5/unit, and anything
above 200 units @ Rs 6/unit. Write a Python program that accepts the units consumed and prints the total electricity bill
(use if-elif and format the amount to 2 decimals). [10 Marks]"""

number_of_units = int(input("Enter the number of units consumed (please enter an integer): "))
is_first_100_units = input("Are the first 100 units consumed? (yes/no): ").strip().lower()

if is_first_100_units == "yes":
    if number_of_units <= 100:
        total_bill = number_of_units * 3
    elif number_of_units <= 200:
        total_bill = (100 * 3) + ((number_of_units - 100) * 4.5)
    else:
        total_bill = (100 * 3) + (100 * 4.5) + ((number_of_units - 200) * 6)
else:
    if number_of_units <= 200:
        total_bill = number_of_units * 4.5
    else:
        total_bill = (200 * 4.5) + ((number_of_units - 200) * 6)

print(f"Total electricity bill: Rs {total_bill:.2f}")