import math
import random

#welcome msg
print("----Welcome To Employee Wage Problem----")

#declare constant
IS_FULL_TIME=1
IS_PART_TIME=2
EMP_RATE_HRS=20

#declare variable for attendence, employeeWage
attendence=math.floor(random.random()*10)%2
empWage=0

#ckeck for employee is present or not
if attendence == IS_FULL_TIME:
    empHrs=8
elif attendence == IS_PART_TIME:
    empHrs=4
else:
    empHrs=0

#calculate employee wage    
empWage=empHrs*EMP_RATE_HRS

#print employee wage
print("Employ Wage: {0}".format(empWage))