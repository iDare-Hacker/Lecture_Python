print("----- Simple Calculator -----")
print("1. Add 2. Subtract 3. Multiply 4. Divide")
choice = int(input("Enter your choice (1-4): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if choice == 1:
    print(f"Result: {a + b}")
elif choice == 2:
    print(f"Result: {a - b}")
elif choice == 3:
    print(f"Result: {a * b}")
elif choice == 4:
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid choice")