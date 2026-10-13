#1. Write a function that takes a list of prices and applies a 10% discount to each price IN PLACE (modifying the original list).

def apply_discount(prices):
    for i in range(len(prices)):
        prices[i] *= 0.9

#2. Write a recursive function to compute the sum of the first n natural numbers.
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

print(sum_natural(5))  # Example usage
