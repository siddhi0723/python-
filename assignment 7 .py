# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Child Class (Inherits from Person)
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        # Call constructor of Person
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def get_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


# Grandchild Class (Inherits from Employee)
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        # Call constructor of Employee
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def get_manager_info(self):
        # Calling methods from parent classes
        self.introduce()
        self.get_employee_info()
        print(f"Department: {self.department}")

    def conduct_meeting(self):
        print(f"Manager is conducting a meeting for the {self.department} department.")


# Creating a Manager object
name = input("Enter Name: ")
age = int(input("Enter Age: "))
employee_id = input("Enter Employee ID: ")
salary = float(input("Enter Salary: "))
department = input("Enter Department: ")

manager1 = Manager(name, age, employee_id, salary, department)

print("\n Manager Details")
manager1.get_manager_info()

print("\n Meeting Info")
manager1.conduct_meeting()