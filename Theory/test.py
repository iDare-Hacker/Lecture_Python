"""#when we apply sorting on the list, does it change indexing

letters = ["d", "a", "c", "b"]

print(letters[0])

letters.sort()  # Sorts the list in place

print(sorted(letters))
print(letters)
print(letters[0])"""

"""list1 = [1, 2, 3, 4, 5]
list1.sort(reverse=True)  # Sorts the list in place in descending order
print(list1)  # Output: [5, 4, 3, 2, 1]

fruits = ["banana", "apple", "cherry", "date"]
fruits.sort(reverse=True)  # Sorts the list in place in descending order
print(fruits)  # Output: ['date', 'cherry', 'banana', 'apple']

fruitlist = fruits.copy()  # Creates a copy of the fruits list

fruitlist.sort()  # Sorts the list in place in ascending order
print(fruitlist)  # Output: ['apple', 'banana', 'cherry', 'date']
print(fruits)  # Output: ['date', 'cherry', 'banana', 'apple'] - only the fruitlist is sorted because it's a separate copy
 #however

fruit1 = fruits
fruits.append("elderberry")  # Modifies the original list
print(fruit1)  # Output: ['date', 'cherry', 'banana', 'apple', 'elderberry'] - /both fruit1 and fruits refer to the same list
print(fruits)  # Output: ['date', 'cherry', 'banana', 'apple', 'elderberry'] - both fruit1 and fruits refer to the same list
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
print(matrix[1])         # [4, 5, 6]  -- the second row 
print(matrix[1][2])      # 6          -- row 1, column 2 
 
students = [ 
    {"name": "Aarav", "marks": 88}, 
    {"name": "Diya", "marks": 45}, 
] 
for s in students: 
    print(s["name"], "-", s["marks"]) 



T1 = (2, 3, 4, 5)
l1 = list(T1)
list.append(l1, 10)
T1 = tuple(l1)
print(T1)  # Output: (2, 3, 4, 5, 10)