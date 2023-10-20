# -------------------------------------------
# Exercise 01 : Classes and objects -- try creating this in oops world
# -------------------------------------------
# Employee
#   # instance variables 
#    emp_id
#    emp_emp_salary
#    mgr_id
#   # class variable 
#   department_name
  
#   # instance methods
#   get_emp_emp_salary()-> emp_emp_salary
#   set_emp_emp_salary(rcv_emp_salary)-> emp_emp_salary

#   # class method 
#   get_department_name() --> department_name
  
#   # static method
#   field_expertise() --> just displays some expertise for all my employees
  
# main:
# main

# 1) create an object employee(100,1000,1)  
# 2) do the following for the created object
# // direct access using .notation
# empid
# emp_emp_salary
# mgr_id
# 3) print the department name 
# 4) display the expertise for the employees 
# 5) Deleting Attributes and Objects



class Employee:
    organisation_name = "GOOGLE"  # Class variable

    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.base_location = base_location
        self.deployed_location = deployed_location
        self.designation = designation
        self.emp_salary = salary

    def get_employee_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Designation: {self.designation}, emp_salary: {self.emp_salary}"

    @classmethod
    def get_organisation_name(cls):
        return cls.organisation_name

    @classmethod
    def set_organisation_name(cls, org_name):
        cls.organisation_name = org_name


class Manager(Employee):
    def __init__(self, emp_id, name, base_location, deployed_location, designation, emp_salary):
        super().__init__(emp_id, name, base_location, deployed_location, designation, emp_salary)
        self.managed_employees = []  # List to store managed employees

    def perform_appraisal_for_an_employee(self, emp_id, percent_raise):
        for employee in self.managed_employees:
            if employee.emp_id == emp_id:
                employee.emp_salary *= (1 + percent_raise / 100)

    def get_manager_details(self, mgr_id):
        return self.get_employee_details() + f", Managed Employees: {len(self.managed_employees)}"


def main():
    # Create three Employee objects
    emp1 = Employee(1001, "corey", "dock_st_1", "california", "sme", 90000)
    emp2 = Employee(1002, "bob", "dock_st_2", "newyork", "consultant", 75000)
    emp3 = Employee(1003, "diana", "dock_st_3", "Brooklyn", "associate", 60000)

    # Create a Manager object and add the Employee objects as managed employees
    manager = Manager(1004, "fluno", "dock_st_4", "california", "manager", 80000)
    manager.managed_employees.extend([emp1, emp2, emp3])

    # Display manager details
    print(manager.get_manager_details(1004))

    # Perform appraisal for an employee (e.g., 101) under the manager
    manager.perform_appraisal_for_an_employee(1002, 1003)
    print("After Appraisal:")
    for emp in manager.managed_employees:
        print(emp.get_employee_details())

if __name__ == "__main__":
    main()
