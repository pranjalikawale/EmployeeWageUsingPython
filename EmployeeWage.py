import math
import random

#welcome msg
print("----Welcome To Employee Wage Problem----")

#declare constant
IS_FULL_TIME=1
IS_PART_TIME=2
EMP_RATE_HRS=20
WORKING_DAY=20

#declare variable for employeeWage
empWage=0

#return fulltime employee working hrs
def isFullTime():
    return 8

#return parttime employee working hrs
def isPartTime():
    return 4    

#return zero employee working hrs
def isAbsent():
    return 0

#ckeck for employee working hrs
switcher={
    0:isAbsent,
    1:isFullTime,
    2:isPartTime,
}

#calculate mothly employee wage
for i in range(1,WORKING_DAY+1):
    #declare variable for attendence
    attendence=math.floor(random.random()*10)%3

    # Get the function from switcher dictionary
    func=switcher.get(attendence)
    
    #calculate employee wage    
    empWage+=func()*EMP_RATE_HRS

#print employee wage
print("Employ Wage for month: {0}".format(empWage))