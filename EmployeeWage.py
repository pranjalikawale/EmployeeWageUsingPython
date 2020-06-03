import math
import random

class EmployWageComputation:

    #welcome msg
    print("----Welcome To Employee Wage Problem----")

    #declare constant
    IS_FULL_TIME=1
    IS_PART_TIME=2

    #declare class variable
    #empRate, numberOfDays, numberOfHrs

    #initialize class variable
    def __init__(self,empRate,numberOfDays,numberOfHrs):
        self.empRate=empRate
        self.numberOfDays=numberOfDays
        self.numberOfHrs=numberOfHrs    

    #return fulltime employee working hrs
    def isFullTime(self):
        return 8

    #return parttime employee working hrs
    def isPartTime(self):
        return 4    

    #return zero employee working hrs
    def isAbsent(self):
        return 0

    switcher={
        0:isAbsent,
        1:isFullTime,
        2:isPartTime,
    }

    #ckeck for employee working hrs
    def getHour():
        #declare variable for attendence
        attendence=math.floor(random.random()*10)%3

        # Get the function from switcher dictionary
        func=switcher.get(attendence)
        return func


    #return daily empWage
    def getDailyWage(self,hrs):
      return (hrs*self.empRate)
    
    #compute employ wage
    def computeEmployeeWage():
        totalWorkingDay=0
        totalWorkingHrs=0 
        hours=0
        #calculate mothly employee wage
        while totalWorkingHrs<self.numberOfHrs  and totalWorkingDay<self.numberOfDays:
            hours=getHour()
            totalWorkingHrs=totalWorkingHrs+hours
            totalWorkingDay+=1
            print(("Employ Wage for day {0} : {1}").format(totalWorkingDay,getDailyWage(hours)))
        #print employee wage    
        print("Employ Wage for month : {0} ".format(getDailyWage(totalWorkingHrs)))

#main
employee=EmployWageComputation(20,20,100)
employee.computeEmployeeWage()