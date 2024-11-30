from manager import Manager
from worker import Worker
from filehandling import FileHandler

def add_employees(employees):
    employee_type = input("Enter Employee Type(manager/worker):").strip().lower()
    name = input("Enter Your Name :")
    age = int(input("Enter Your Age :"))
    salary = int(input("Enter Your Salary :"))
    if employee_type == 'manager':
        department = input("Enter Your Department :")
        employees.append(Manager(name, age, salary, department))
    elif employee_type == 'worker':
        hours_worked = int(input("Enter Hours Worked :"))
        employees.append(Worker(name, age, salary, hours_worked))

def diplay_employees(employees):
    for employee in employees:
        employee.display_info()
        print('-' * 20) 

def update_employee(employees):
    name = input("Enter Name to Update :")
    for employee in employees:
        if employee.get_name() == name:
            attribute = input("Enter Attribute to Update(name/age/salary/department/hours_worked) :").strip().lower()
            if attribute == 'name':
                employee.set_name(input("Enter New Name :"))
            elif attribute == 'age':
                employee.set_age(int(input("Enter New Age :")))
            elif attribute == 'salary':
                employee.set_salary(int(input("Enter New Salary :")))
            elif attribute == 'department' or isinstance(employee, Manager):
                employee.set_department(input("Enter New Department :"))
            elif attribute == 'hours_worked' or isinstance(employee, Worker):
                employee.set_hours_worked(int(input("Enter Updated Hours Worked :")))
            break
        
def delete_employee(employees):
    name = input("Enter name to delete :")
    for i, employee in enumerate(employees):
        if employee.get_name() == name:
            del employees[i]
            break

def main_menu():
    filename = 'employees.csv'
    employees = FileHandler.load_employees(filename)

    while True:
        print("<<<<<<<Menu Bar>>>>>>>")
        print("1- Add Employee")
        print("2- Display Employee")
        print("3- Update Employee")
        print("4- Delete Employee")
        print("5- Save") 
        print("6- Exiting") 

        choice = input("Enter Your Choice :")

        if choice == '1':
            add_employees(employees)
        elif choice == '2':
            diplay_employees(employees)
        elif choice == '3':
            update_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            FileHandler.save_employees(employees, filename)
        elif choice == '6':
            print("Exiting")
            break

if __name__ == "__main__":
    main_menu()                      