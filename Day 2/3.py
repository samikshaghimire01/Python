# Create an abstract base class Employee (use ABC) with:
# Abstract method calculate_salary()
# Abstract method get_role()
# Concrete method display_info() that uses the abstract methods
# Class variable company_name
# Create inheritance hierarchy:
# Employee
# ├── FullTimeEmployee (has annual_salary, benefits)
# │   └── Manager (has team_size, bonus_percentage)
# │       └── Director (has department, additional_stock_options)
# └── ContractEmployee (has hourly_rate, hours_worked, contract_duration)
# Each subclass must:
# Implement all abstract methods differently
# Override work() method with specific behavior
# Call parent's init using super()
# Add at least one unique method
# Demonstrate:
# Polymorphism: store different employee types in a list and call methods
# Method resolution order (MRO) by printing it
# Creating instances of all concrete classes (not abstract Employee)
# Show how each calculates salary differently



from abc import ABC, abstractmethod

class Employee(ABC):
    company_name = "GrowbyData"

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

    def work(self):
        print(f"{self.name} is working.")

    def display_info(self):
        print(f"""
Company : {Employee.company_name}
Name    : {self.name}
Role    : {self.get_role()}
Salary  : ${self.calculate_salary()}
""")


# Full Time Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary, benefits):
        super().__init__(name)
        self.annual_salary = annual_salary
        self.benefits = benefits

    def calculate_salary(self):
        return self.annual_salary / 12

    def get_role(self):
        return "Full-Time Employee"

    def work(self):
        print(f"{self.name} works full-time.")

    def show_benefits(self):
        print(f"Benefits: {self.benefits}")


# Manager
class Manager(FullTimeEmployee):
    def __init__(self, name, annual_salary, benefits, team_size, bonus_percentage):
        super().__init__(name, annual_salary, benefits)
        self.team_size = team_size
        self.bonus_percentage = bonus_percentage

    def calculate_salary(self):
        base = super().calculate_salary()
        bonus = base * (self.bonus_percentage / 100)
        return base + bonus

    def get_role(self):
        return "Manager"

    def work(self):
        print(f"{self.name} manages a team of {self.team_size} employees.")

    def conduct_meeting(self):
        print("Conducting team meeting.")


# Director
class Director(Manager):
    def __init__(self, name, annual_salary, benefits, team_size, bonus_percentage, department, additional_stock_options):
        super().__init__(name, annual_salary, benefits, team_size, bonus_percentage)
        self.department = department
        self.additional_stock_options = additional_stock_options

    def calculate_salary(self):
        return super().calculate_salary() + self.additional_stock_options

    def get_role(self):
        return "Director"

    def work(self):
        print(f"{self.name} leads the {self.department} department.")

    def strategic_planning(self):
        print("Performing strategic planning.")


# Contract Employee
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked, contract_duration):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.contract_duration = contract_duration

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_role(self):
        return "Contract Employee"

    def work(self):
        print(f"{self.name} works on a contract basis.")

    def contract_details(self):
        print(f"Contract Duration: {self.contract_duration} months")


fte = FullTimeEmployee("JayRam Raut", 120000, ["Health Insurance", "Paid Leave"])
manager = Manager("Nirmala", 180000, ["Health Insurance", "Bonus"], 10, 15)
director = Director("Rajan", 250000, ["All Benefits"], 25, 25, "Engineering", 5000)
contractor = ContractEmployee("Hemraj", 50, 160, 6)

employees = [fte, manager, director, contractor]

for emp in employees:
    emp.display_info()
    emp.work()


print("\nMethod Resolution Order (MRO) for Director:")
print(Director.mro())
