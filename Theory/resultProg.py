#program to find the grade of a student based on marks
from statistics import mean


marks = int(input("enter the marks from 0-100: "))


if marks>=75 and marks <= 100:
   grade = "distiction"
elif marks>=60:
   grade = "first class"
elif marks>=50:
   grade = "second class"
elif marks>=35:
   grade = "pass"
elif marks>=0:
   grade = "fail"
else:
   grade = "invalid input"

print(grade)