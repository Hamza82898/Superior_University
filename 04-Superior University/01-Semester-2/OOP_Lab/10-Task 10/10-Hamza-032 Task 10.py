import csv


class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_salary(self):
        return self.__salary
    
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age 
    
    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        print("Name :", self.__name)
        print("Age :", self.__age)
        print("Salary :", self.__salary)

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def display_info(self):
        super().display_info()
        print("Department :", self.__department)


class Worker(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked

    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    def display_info(self):
        super().display_info()
        print("Hours Worked :", self.__hours_worked) 


class FileHandler:
    def save_employees(employees, filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "age", "salary", "department", "hours_worked"])
            for employee in employees:
                if isinstance(employee, Manager):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(),"", employee.get_department()])
                elif isinstance(employee, Worker):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), employee.get_hours_worked()]) 

    def load_employees(filename):
        employees = []
        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    name, age, salary, department, hours_worked = row
                    # name = row.get("name")
                    # age = int(row.get["age", 0])
                    # salary = int(row.get["salary", 0])
                    # department = row.get("department", None)
                    # hours_worked = int(row.get["hours_worked", None])

                    if department:
                        employees.append(Manager(name, int(age), int(salary), department))
                    elif hours_worked:
                        employees.append(Worker(name, int(age), int(salary), int(hours_worked)))
        except FileNotFoundError:
            print(f"File {filename} Not Found. Create First.")
        return employees




def add_employee(employees):
    employee_type = input("Enter Employee Type(Manager/Worker) :").strip().lower()
    name = input("Enter Your Name :")
    age = int(input("Enter Your Age :"))
    salary = int(input("Enter Your Salary :"))
    if employee_type == "manager":
        department = input("Enter Your Department :")
        employees.append(Manager(name, age, salary, department))
    elif employee_type == "worker":
        hours_worked = int(input("Enter Hours Worked :"))
        employees.append(Worker(name, age, salary, hours_worked))

def display_employees(employees):
    for employee in employees:
        employee.display_info()
        print("-" * 20)

def update_employee(employees):
    name = input("Enter the name of Employee to update :")
    for employee in employees:
        if employee.get_name() == name:
            attribute = input("Enter Attribute to update(name/age/salary/department/hours_worked) :").strip().lower()
            if attribute == "name":
                employee.set_name(input("Enter New Name :"))
            elif attribute == "age":
                employee.set_age(int(input("Enter New Age :")))
            elif attribute == "salary":
                employee.set_salary(int(input("Enter New Salary :")))
            elif attribute == "department" and isinstance(employee, Manager):
                employee.set_department(input("Enter New Department :"))
            elif attribute == "hours_worked" and isinstance(employee, Worker):
                employee.set_hours_worked(int(input("Enter New Hours Worked :")))
            else:
                print(f"Employee {name} not found!")    
            break

def delete_employee(employees):
    name = input("Enter Name to Delete :")
    for i, employee in enumerate(employees):
        if employee.get_name() == name:
            del employees[i]
            break

def main():
    filename = "employees.csv"
    employees = FileHandler.load_employees(filename)

    while True:
        print("1. Add Employee")
        print("2. Display Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save")
        print("6- Exit.")
        choice = input("Enter your Choice :")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            display_employees(employees)
        elif choice == "3":
            update_employee(employees)
        elif choice == "4":
            delete_employee(employees)
        elif choice == "5":
            FileHandler.save_employees(employees, filename)
        elif choice == "6":
            print("Exit")
            return    
        else:
            print("Invalid Choice!!! Please Enter A Correct Choice.....")
            

if __name__ == "__main__":
    main()                          