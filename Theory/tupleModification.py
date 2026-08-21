# Convert immutable tuple to list -> modify -> convert back to tuple
T1 = (2, 3, 4, 5)

l1 = list(T1)
l1.append(10)
T1 = tuple(l1)

print("Updated Tuple:", T1)  # Output: (2, 3, 4, 5, 10)

