import csv

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Position: {self.position}")

class Staff(Person,Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def additional_info(self):
        print(f"Department: {self.department}")



def save_employee(staff_list):
    with open("employees.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name","Age","Employee ID","Position","Department"])
        for staff in staff_list:
            writer.writerow([staff.name, staff.age, staff.employee_id, staff.position, staff.department])

def read_employee():
    staff_list = []
    try:
        with open("employees.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                staff = Staff(
                    name = row["Name"],
                    age = int(row["Age"]),
                    employee_id = row["Employee ID"],
                    position = row["Position"],
                    department = row["Department"]
                )
                staff_list.append(staff)
    except FileNotFoundError:
        print("File Not Found. Create New File..")
    return staff_list

def add_employee(staff_list):
    name = input("Enter Your Name:")
    age = int(input("Enter Your Age:"))
    employee_id = input("Enter Your Employee ID:")
    position = input("Enter Your Position:")
    department = input("Enter Your Department")
    staff = Staff(name, age, employee_id, position, department)
    staff_list.append(staff) 

if __name__ == "__main__":
    employees = read_employee()
    while True:
        print("\nMenu")
        print("1- Add Employee.")
        print("2- Display Employee.")
        print("3- Save and Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            for emp in employees:
                emp.display_info()
                emp.additional_info()
        elif choice == "3":
            save_employee(employees)
            print("Saved Successfully! Existing......")
            break
        else:
            print("Invalid Choice! Enter a Valid Choice.")                                           

