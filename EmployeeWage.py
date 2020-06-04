import math
import random

class EmployWageComputation:

    #welcome msg
    print("----Welcome To Employee Wage Problem----")

    #declare constant
    IS_FULL_TIME=1
    IS_PART_TIME=2

    #initialize class variable
    def __init__(self,emp_rate,number_of_days,number_of_hrs):
        self.emp_rate=emp_rate
        self.number_of_days=number_of_days
        self.number_of_hrs=number_of_hrs    

    #return fulltime employee working hrs
    def is_full_time(self):
        return 8

    #return parttime employee working hrs
    def is_part_time(self):
        return 4    

    #return zero employee working hrs
    def is_absent(self):
        return 0

    #switcher to select one of the option
    switcher={
        0:is_absent,
        1:is_full_time,
        2:is_part_time,
    }

    #ckeck for employee working hrs
    def get_hour(self):
        #declare variable for attendence
        attendence=math.floor(random.random()*10)%3

        # Get the function from switcher dictionary
        func=self.switcher.get(self,attendence)
        return func


    #return daily empWage
    def get_daily_wage(self,hrs):
      return (hrs*self.emp_rate)
    
    #compute employ wage
    def compute_employee_wage(self):
        total_working_day=0
        total_Working_hrs=0 
        hours=0

        #calculate mothly employee wage
        while total_Working_hrs<self.number_of_hrs  and total_working_day<self.number_of_days:
            hours=self.get_hour()
            total_Working_hrs+=hours
            total_working_day+=1
            print(("Employ Wage for day {0} : {1}").format(total_working_day,self.get_daily_wage(hours)))

        #print employee wage    
        print("Employ Wage for month : {0} ".format(self.get_daily_wage(total_Working_hrs)))

#main
employee=EmployWageComputation(20,20,100)
employee.compute_employee_wage()