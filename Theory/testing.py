
"""
from sympy import isprime, primerange
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)
"""

"""
num = int(input("Enter a number: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is Prime")
else:
    print(f"{num} is Not Prime")
"""


"""
#find the greatest number among three numbers
a = int(input("enter the number: "))
b = int(input("enter the number: "))
c = int(input("enter the number: "))


print("The largest number is:", max(a, b, c))
print("The largest number is:", mean([a, b, c]))


#list1 = [a, b, c]
#list1.sort()
#print("The largest number is:", list1[-1])
"""



"""n = int(input("How many terms? "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print() # move to a new line at the end
"""

