""""1. Write a program to display a bill with item name, quantity, price, and total, neatly formatted using f-strings.

2. Write a program to check whether a number is divisible by both 3 and 5 using logical operators."""

#1
lst = {
    "item_name_lst": ["item1", "item2", "item3"],
    "quantity_lst": [2, 3, 1],
    "price": [120,150.5,190]}
print("-"*23,"Bill","-"*23)
print(f"{'Item':<15}{'quantity':<10}{'Price':>10}{'Total Price':>15}")

for i in lst["item_name_lst"]:
    index = lst["item_name_lst"].index(i)
    print(f"{lst["item_name_lst"][index]:<15}{lst["quantity_lst"][index]:<10}{lst["price"][index]:>10}{lst["quantity_lst"][index]*lst["price"][index]:>15}")

total = 0
for n in lst["item_name_lst"]:
    index = lst["item_name_lst"].index(i)
    total = total + lst["quantity_lst"][index]*lst["price"][index]
print(f"{'Total':<25}{total:>25}")

print()

#2
number = int(input("Enter a number: "))
if number%5 == 0 and number%3 == 0:
    print("The number:", number, "is divisable by both 3, and 5")
else:
    print("The number:", number, "is not divisable by both 3, and 5")