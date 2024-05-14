from datetime import datetime
#Employee Management System
# You are tasked to build an employee management system for a small business.

# The system allows the business to store and manage employee data, and perform tasks related to employee management, such as
# adding and removing employees, updating employee information, searching for employees by name or department, and calculation total salary
# expenses.
# You will need to create one class for this project:

# Employee, which represents a single employee'''

class Employee:
    #Constructor
    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary =  salary
        self.hire_year =  hire_year

    #String Method            
    def __str__(self):
        return (f'Employee name: {self.name}\nJob title: {self.job_title}\nDepartment: {self.department}\nSalary: ${self.salary:.02f}\nYear hired: {self.hire_year}')
    
    #Total years worked
    def years_worked(self):
       present_year = datetime.now().year
       years_worked = present_year - self.hire_year
       return f'{self.name} has worked for {years_worked} years'
    
    #Total expense
    def total_expense(self):
        total_expense = 20 * self.salary
        return f'{self.name} total salary is ${total_expense}'
   

    #Text file
    def print_write_employees(self):
        f = open("write_employees.txt", "w")
        f.write(f'''Employee name: {self.name}\nJob title: {self.job_title}\nDepartment: {self.department}\nSalary: ${self.salary:.02f}\nYear hired: {self.hire_year}''')
        f.close()
                
    #accessor method for all attributes
    def get_name(self):
        return self.name
    def get_job_title(self):
        return self.job_title
    def get_department(self):
        return self.department
    def get_salary(self):
        return self.salary
    def get_hire_year(self):
        return self._hire_year  
  
    #  #mutator method for all attributes
    def set_name(self, new_name):
        self.name = new_name
    def set_job_title(self, new_job_title):
        self.job_title = new_job_title
    def set_department(self, new_department):
        self.department = new_department
    def set_salary(self, new_salary):
        self.salary = new_salary
    def set_hire_year(self, new_hire_year):
        self.hire_year = new_hire_year


employee1 = Employee('Brenetta','Manager','Human Resource', 80000, 2004)

 #String representation 

# print(employee1)
# print(employee1.years_worked())
# print(employee1.total_expense())
# employee1.print_write_employees()


