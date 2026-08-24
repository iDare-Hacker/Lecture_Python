#=======================================
#          5 Mark Question
#=======================================
#---------------------------------------
#                 Set 1
#--------------------------------------

#Q1
number = "25"
number = int(number)
number += 10
print(number)
print(type(number))

#Q2
word = "Data"
print(word * 3)  # The * operator when used with a string and a number
# repeats the string the specified number of times. In this case, it repeats "Data"
# three times, resulting in "DataDataData".

#Q3
lst = [1, 2, 3]
lst2 = lst  # lst2 is a reference to the same list object as lst
lst2.append(4)
print(lst)  # Output: [1, 2, 3, 4]
print(lst2)  # Output: [1, 2, 3, 4]
# Both lists changed because lst2 is not a copy of lst; it is a reference to the same list object in memory. Therefore, any modifications made to lst2 also affect lst.

#Q4
s = {1, 2, 2, 3, 3, 3}
print(s)  # Output: {1, 2, 3}
print(len(s))  # Output: 3
# The duplicate values in the set are automatically removed because sets only store unique elements. Therefore, the final set contains only the unique values {1, 2, 3}, and its length
# is 3.


#---------------------------------------
#                 Set 2
#--------------------------------------
#Q1
x = 7
y = 2
print(x / y)  # Output: 3.5
print(x // y)  # Output: 3
# The / operator always gives a float result, while the // operator gives an integer result (floor division).

#Q2
sentence = input("Enter a sentence: ")
if len(sentence) > 0:
    first_char = sentence[0]
    last_char = sentence[-1]
    print("First character:", first_char)
    print("Last character:", last_char)
else:
    print("The sentence is empty.")

#Q3
original_list = [1, 2, 3]
# Copying the list using slicing
copied_list = original_list[:]  # or you can use original_list.copy()
copied_list.append(4)
print("Original list:", original_list)  # Output: [1, 2, 3]
print("Copied list:", copied_list)  # Output: [1, 2, 3, 4]
# The original list remains unchanged after appending to the copied list

#Q4
existing_set = {1, 2, 3}
new_elements = [4, 5, 6]
existing_set.update(new_elements)
print("Updated set:", existing_set)  # Output: {1, 2, 3, 4, 5, 6}

#---------------------------------------
#                 Set 3
#--------------------------------------
#Q1
a = 5
b = a
b += 3
print("Value of a:", a)  # Output: 5
print("Value of b:", b)  # Output: 8
# Changing b did not affect a because integers are immutable in Python. 
# When we assigned b = a, b got a copy of the value of a. Therefore, modifying b does not change the value of a.

#Q2
user_string = input("Enter a string: ")
index_to_access = 10  # Example index to access
if len(user_string) > index_to_access:
    print("Character at index", index_to_access, ":", user_string[index_to_access])
else:
    print("The string is too short to access index", index_to_access)

#Q3
t = (1, 2, 3)
temp_list = list(t)
temp_list[0] = 10
t = tuple(temp_list)
print("Final tuple:", t)

#Q4
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print("Updated set1:", set1)

#---------------------------------------
#                 Set 4
#--------------------------------------
#Q1
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.") 

#Q2
word = "concatenate"
if "cat" in word:
    print("The substring 'cat' exists in the word 'concatenate'.")
else:
    print("The substring 'cat' does not exist in the word 'concatenate'.")

#Q3
lst = [5, 3, 8, 1, 9]
print("lst[-1]:", lst[-1])  # Output: 9, refers to the last element of the list
print("lst[-3]:", lst[-3])  # Output: 8, refers to the third element from the end of the list

#Q4
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)  # Removes 3 from the set
print("Set after discarding 3:", my_set)  # Output: {1, 2, 4, 5}
my_set.discard(10)  # Attempting to discard an element not present in the set
print("Set after attempting to discard 10:", my_set)  # Output: {1, 2, 4, 5}, no error raised


#=======================================
#          10 Mark Question
#=======================================


#---------------------------------------
#                 Set 5
#--------------------------------------
#Q1
set_A = {101, 102, 103, 104, 105} 
set_B = {104, 105, 106, 107} 

set_union = set_A.union(set_B)
print("Union of sets A and B:", set_union)
set_intersection = set_A.intersection(set_B)
print("Intersection of sets A and B:", set_intersection)
set_only_python = set_A.difference(set_B)
print("Students who appeared for ONLY the Python test:", set_only_python)


#Q2
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