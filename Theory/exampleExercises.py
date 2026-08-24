from statistics import mean
#from sympy import isprime, primerange

# ==========================================
# 1. FACTORIAL CALCULATOR
# ==========================================
def calculate_factorial():
    """Calculates the factorial of a given number using a loop."""
    num = int(input("Enter a number for factorial: "))
    factorial = 1
    
    # Multiply numbers sequentially from 1 to num
    for i in range(1, num + 1):
        factorial *= i
        
    print(f"Factorial of {num} is: {factorial}\n")


# ==========================================
# 2. PRIME NUMBER CHECKER
# ==========================================
def check_prime():
    """Checks whether a given number is prime using trial division."""
    num = int(input("Enter a number to check prime: "))
    is_prime = True
    
    # Numbers less than 2 are not prime
    if num < 2:
        is_prime = False
    else:
        # Check divisibility up to num - 1
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
                
    if is_prime:
        print(f"{num} is Prime\n")
    else:
        print(f"{num} is Not Prime\n")


# ==========================================
# 3. GREATEST OF THREE NUMBERS
# ==========================================
def find_largest_number():
    """Finds the maximum value among three input numbers."""
    a = int(input("Enter first number (a): "))
    b = int(input("Enter second number (b): "))
    c = int(input("Enter third number (c): "))

    # Method 1: Using max()
    print("The largest number is:", max(a, b, c))
    
    # Mean calculation (Separated to clarify intent)
    print("The average (mean) is:", mean([a, b, c]))

    # Method 2 (Alternative): Sorting a list
    # list1 = [a, b, c]
    # list1.sort()
    # print("The largest number is:", list1[-1])
    print()


# ==========================================
# 4. FIBONACCI SERIES GENERATOR
# ==========================================
def generate_fibonacci():
    """Generates the Fibonacci series up to 'n' terms."""
    n = int(input("How many Fibonacci terms? "))
    a, b = 0, 1
    
    print("Fibonacci sequence:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Update values for the next term
    print("\n")


# ==========================================
# MAIN EXECUTION MENU
# ==========================================
if __name__ == "__main__":
    print("=== BASIC PYTHON PROGRAMS ===\n")
    
    calculate_factorial()
    check_prime()
    find_largest_number()
    generate_fibonacci()