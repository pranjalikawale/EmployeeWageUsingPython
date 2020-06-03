import math
import random

#welcome msg
print("----Welcome To Employee Wage Problem----")

#declare constant
IS_FULL_TIME=1
EMP_RATE_HRS=20

#declare variable for attendence, employeeWage and employeeHrs
attendence=math.floor(random.random()*10)%2
empWage=0
empHrs=0

#ckeck for employee is present or not
if attendence == IS_FULL_TIME:
    empHrs=8

#calculate employee wage    
empWage=empHrs*EMP_RATE_HRS

#print employee wage
print("Employ Wage: {0}".format(empWage))