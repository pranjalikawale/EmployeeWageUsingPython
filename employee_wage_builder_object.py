from employee_wage import EmployWageComputation

class EmployeeWageBuilderObject():
    tcs=EmployWageComputation("TCS",20,20,100)
    jio=EmployWageComputation("JIO",20,20,100)
    tcs.compute_employee_wage()
    tcs.total_employee_wage()
    jio.compute_employee_wage()
    jio.total_employee_wage()
    