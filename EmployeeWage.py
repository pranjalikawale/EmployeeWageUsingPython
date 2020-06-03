import math
import random

print("----Welcome To Employee Wage Problem----")

IS_FULL_TIME=1
attendence=math.floor(random.random()*10)%2

if attendence == IS_FULL_TIME:
    print("Employee is Present")
else:
    print("Employee is Absent")