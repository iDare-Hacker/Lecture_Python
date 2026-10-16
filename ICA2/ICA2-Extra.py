
##################################################
# ICA2 - 1 Questions 10 Marks Each
####################################################

"""Write a function fib_list(n) that returns a list of the first n Fibonacci numbers using a loop, and a recursive function
fib(n) that returns the nth term (fib(0) = 0, fib(1) = 1). Print both for n = 10 and verify that they agree, then print the ratio
of each term to the previous one (from the third term onward) to 3 decimals. [10 Marks]"""
def fib_list(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n+1):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fib(n):
    """Return the nth Fibonacci number recursively."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

x = 10
print(f"First {x} Fibonacci numbers (using loop): {fib_list(x)}")
print(f"The {x}th Fibonacci number (using recursion): {fib(x)}")

"""fib_list(10) returns the first 11 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], 
the reason for 11 numbers is because the function includes the 0th term, therefore in the loop I added 1 to n in the range.
allowing the 10th index to be included in the list. (starting from 0, the 10th index corresponds to the 11th Fibonacci number).

fib(10) returns the 10th Fibonacci number: 55
which is the same as the last number in the list returned by fib_list(10), confirming that both functions agree.
the 10th index of the fib_list corresponds to the 10th Fibonacci number, which is 55.
"""

i = int(input("Enter the value of n to calculate the ratio of each term to the previous one (from the third term onward): "))
if i < 3:
    print("Please enter a value of n greater than or equal to 2.")
else:
    fib_sequence = fib_list(i)
    print(f"Fibonacci sequence up to {i} terms: {fib_sequence}")
    print("Ratios of each term to the previous one (from the third term onward):")
    for j in range(2, i + 1):
        ratio = fib_sequence[j] / fib_sequence[j - 1]
        print(f"Ratio of term {j} to term {j-1}: {ratio:.3f}")

