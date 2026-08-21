# 1. Sorting and Indexing
letters = ["d", "a", "c", "b"]

print("Original index 0:", letters[0])  # Output: d

# sorted() creates a new list, leaves original untouched
print("Sorted copy:", sorted(letters))  # Output: ['a', 'b', 'c', 'd']
print("Original list:", letters)        # Output: ['d', 'a', 'c', 'b']

# .sort() modifies the list in-place, changing item positions/indexes
letters.sort()
print("Original list after .sort():", letters)  # Output: ['a', 'b', 'c', 'd']
print("New index 0:", letters[0])               # Output: a


# 2. Descending Sort
list1 = [1, 2, 3, 4, 5]
list1.sort(reverse=True)
print("Descending list:", list1)  # Output: [5, 4, 3, 2, 1]


# 3. Copying vs. Aliasing
fruits = ["banana", "apple", "cherry", "date"]
fruits.sort(reverse=True)

# .copy() creates an independent copy
fruitlist = fruits.copy()
fruitlist.sort()
print("Sorted copy:", fruitlist)  # Output: ['apple', 'banana', 'cherry', 'date']
print("Original list:", fruits)   # Output: ['date', 'cherry', 'banana', 'apple']

# Reference assignment (aliasing): both point to the same list in memory
fruit1 = fruits
fruits.append("elderberry")
print("Alias variable:", fruit1)  # Contains 'elderberry'
print("Original variable:", fruits)  # Contains 'elderberry'


# 4. Indexing with Positive and Negative Indices
fruits = ["apple", "banana", "cherry", "date"]

# Positive index (starts from 0)
print("First item:", fruits[0])   # Output: apple

# Negative index (starts from -1 at the end)
print("Last item:", fruits[-1])  # Output: date



# 5. List Modification Methods
numbers = [1, 2, 3]

# Append: Add single item to the end
numbers.append(4) 

# Insert: Add single item at specific index (index 1)
numbers.insert(1, 1.5) 

# Extend: Merge multiple elements from another iterable
numbers.extend([5, 6])

print("Updated list:", numbers) # Output: [1, 1.5, 2, 3, 4, 5, 6]



# 6. Removing Items from a List
items = ["A", "B", "C", "D", "E"]

# .remove(): Delete by value (removes first matching occurrence)
items.remove("B") 

# .pop(): Remove and return element by index (defaults to last item)
last_item = items.pop() 
specific_item = items.pop(0)

print("Remaining items:", items)      # Output: ['C', 'D']
print("Popped last item:", last_item) # Output: E
print("Popped item at 0:", specific_item) # Output: A