#Employee Management System
# You are tasked to build an employee management system for a small business.

# The system allows the business to store and manage employee data, and perform tasks related to employee management, such as
# adding and removing employees, updating employee information, searching for employees by name or department, and calculation total salary
# expenses.
# You will need to create one class for this project:

# Employee, which represents a single employee'''

class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
        se


    def __str__(self):
        return f'{self.name} works in {self.department} and makes {self.salary}'
    
employee1 = Employee('Sandra','Accounting', 50000 )
employee2 = Employee('Thomas', 'Finance', 80000)
employee3 = Employee('Candice', 'Human Resource', 120000)




print(employee3)