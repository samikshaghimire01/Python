# Create an Employee class with class variable company = "GrowByData"
# Implement a classmethod to change company name with validation:
   
# Must be 3-50 characters
# Must contain only letters, numbers, and spaces
# Add instance attributes: name, email, employee_id, salary, department
# Implement a classmethod to generate unique employee IDs (format: EMP-YYYY-XXXX)
# Add a class variable to track all employees and department counts


import datetime
import re

class Employee:
    
    company = "GrowByData"
    employees = []           
    department_count = {}    
    _id_counter = 1          

    def __init__(self, name, email, salary, department):
        self.name = name
        self.email = email
        self.salary = salary
        self.department = department
        self.employee_id = self.generate_employee_id()
        
        Employee.employees.append(self)
        Employee.department_count[department] = Employee.department_count.get(department, 0) + 1

    @classmethod
    def change_company(cls, new_name):

        if 3 <= len(new_name) <= 50 and re.match(r'^[A-Za-z0-9 ]+$', new_name):
            cls.company = new_name
            print(f"Company name changed to: {cls.company}")
        else:
            raise ValueError("Invalid company name. Must be 3-50 chars and contain only letters, numbers, spaces.")

    @classmethod
    def generate_employee_id(cls):

        year = datetime.datetime.now().year
        emp_id = f"EMP-{year}-{cls._id_counter:04d}"
        cls._id_counter += 1
        return emp_id

    def __str__(self):
        return f"{self.employee_id} | {self.name} | {self.department} | ${self.salary}"


emp1 = Employee("Aryan Khan", "aryan@growbydata.com", 80000, "Marketing")
emp2 = Employee("Ananya Pandey", "ananya@growbydata.com", 80000, "Marketing")
emp3 = Employee("Lovely Singh", "lovely@growbydata.com", 60000, "Entertainment")


for emp in Employee.employees:
    print(emp)

print("\nDepartment Counts:", Employee.department_count)

Employee.change_company("NextGen Data")
