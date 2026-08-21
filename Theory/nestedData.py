# 1. 2D List (Matrix) Access
matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
] 

print("Row 1:", matrix[1])         # Output: [4, 5, 6]
print("Row 1, Col 2:", matrix[1][2]) # Output: 6


# 2. List of Dictionaries Iteration
students = [ 
    {"name": "Aarav", "marks": 88}, 
    {"name": "Diya", "marks": 45}, 
] 

for student in students: 
    print(student["name"], "-", student["marks"])