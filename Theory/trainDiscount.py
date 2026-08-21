#to find discount on train tickets
#First point ask user weather railway employee or not
#for railway employee discount is 30%
#for others user if age is less than 18 20% discount
#elif senior citizen age is greater than 60 25% discount
# for rest 5 % discount


is_railway_employee = input("Are you a railway employee? (yes/no): ")
if is_railway_employee == "yes":
   discount = 30
else:
   age = int(input("Enter your age: "))
   if age < 18:
       discount = 20
   elif age > 60:
       discount = 25
   else:
       discount = 5


print(f"You are eligible for a discount of {discount}%.")