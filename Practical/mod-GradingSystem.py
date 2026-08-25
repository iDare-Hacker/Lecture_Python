marks = 0
for i in range(1,6):
    is_input_valid = False
    while(not(is_input_valid)):
        mark= int(input("please enter the marks for test "))
        if mark > 100 or mark < 0:
             print("invalid input")
             is_input_valid = False
        else:
            marks = marks + mark
            is_input_valid = True

marks = marks/5

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)