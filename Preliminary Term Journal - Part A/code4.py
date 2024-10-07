"""
Create function Employee details with user define data like
empid, empname, empqualification, empdesignation, empsalary,
emp_currentmonthrank. If current month rank is >4 than add 
incentive Rs.2500 in salary.
"""

class EmployeeDetails:
    def __init__(self, empid, empname, empqualification, empdesignation, empsalary, emp_currentmonthrank):
        self.empsalary = empsalary + 2500 if emp_currentmonthrank > 4 else empsalary
        self.empid = empid
        self.empname = empname
        self.empqualification = empqualification
        self.empdesignation = empdesignation

    def display_details(self):
        print(self.empid, self.empname, self.empqualification, self.empdesignation, self.empsalary)

e1 = EmployeeDetails(123, "Tanmay", "BCA", "Dev", 10000, 5)
e2 = EmployeeDetails(123, "Tejas", "Btech", "Dev", 7000, 3)

e1.display_details()
e2.display_details()
