def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y. Raises ValueError if y is zero."""
    return x / y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


while True:
    selction = input("Select operation (add, subtract, multiply, divide): ")

    if selction == "add":
        print(f"The sum of {x} and {y} is: {add(x, y)}")
        break
    elif selction == "subtract":
        print(f"The difference of {x} and {y} is: {subtract(x, y)}")
        break
    elif selction == "multiply":
        print(f"The product of {x} and {y} is: {multiply(x, y)}")
        break
    elif selction == "divide":
        if y == 0:
            print("Cannot divide by zero. Please enter a non-zero second number.")
        else:
            result = divide(x, y)
            print(f"The quotient of {x} and {y} is: {result}")
        break
    else:
        print("Invalid operation selected.")
