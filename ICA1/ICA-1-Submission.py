#Dev Kamdar Roll No: A008 Set 5, 4 questions each 5 marks, total 20 marks

#Q1. [Data Types & Operators] Take two numbers as string input (e.g. "12" and "8"). First print them joined with + (string concatenation), then convert both to int and print their sum, clearly showing the difference. [5 Marks]

num1 = 12
num2 = 8

print("String concatenation:", str(num1) + str(num2))  
"""to use the + for string conatination 
we need to convert the value into string using type conversion
if don't it will give us an sum"""
print("Sum of integers:", num1 + num2) 



#Q2. [Strings] Let name = "NMIMS". Print name[::2] (every second character) and explain in a comment what slicing patternwas used. [5 Marks]

name = "NMIMS"
print(name[::2])  

"""This slicing pattern takes every second character from the string, 
 starting from index 0 (N), 
 then index 2 (I), (skiping index 1) 
 and finally index 4 (skipping index 3), 
 resulting in the output "NIS"."""

#Strings are basicaly a list of characters. 
#Therefore we can use indexing on them allowing us to access individual characters or slices of the string.




#Q3. [Lists & Tuples] Write a program to insert the number 99 at position 2 of a list using insert(), then remove and print the LAST element using pop(). [5 Marks]
list_example = [1, 2, 3, 4, 5]
list_example.insert(1, 99)  # Inserts 99 at index 1 (which is position 2) #shifts elemets
print("List after insertion:", list_example)

"""There are two ways to do so,
one way in to store the popped element in a variable and then print it,
another way is to directly print the popped element without storing it in a variable."""
#method 1:
#last_element = list_example.pop() 
#print("Removed last element:", last_element)

#method 2:
print("Removed last element:", list_example.pop())

print("List after removing last element:", list_example)



#Q4. [Sets & Dictionaries] Take a list containing duplicate values, convert it into a set to remove duplicates, then convert it back into a SORTED list and print the final result. [5 Marks]
list_duplicates = [5, 3, 8, 3, 2, 5, 1, 8]
set_unique = set(list_duplicates)  
sorted_list = list(sorted(set_unique)) 
print("Final sorted list without duplicates:", sorted_list)