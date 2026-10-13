#1. Write a function is_prime(n) that returns True or False.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#2. Write a function that accepts any number of arguments and returns their average using *args.
def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)


print(is_prime(11))  # Example usage
print(average(1, 2, 3, 4, 5))  # Example usage

while True:
    try:
        x =int(input("How many numbers do you want to enter: "))
        if x <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")


input_numbers = []
for i in range(x):
    num = float(input(f"Enter number {i + 1}: "))
    input_numbers.append(num)

print(f"The average of the entered numbers is: {average(*input_numbers)}")
