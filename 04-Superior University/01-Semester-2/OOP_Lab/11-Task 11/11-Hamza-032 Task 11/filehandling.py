from manager import Manager
from worker import Worker
import csv

class FileHandler:
    def save_employees(employees, filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for employee in employees:
                if isinstance(employee, Manager):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), employee.get_department()])
                elif isinstance(employee, Worker):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), employee.get_hours_worked()]) 

    def load_employees(filename):
        employees = []
        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    name, age, salary, department, hours_worked = row
                    if department:
                        employees.append(Manager(name, int(age), int(salary), department))
                    elif hours_worked:
                        employees.append(Worker(name, int(age), int(salary), int(hours_worked)))
        except FileNotFoundError:
            print("File Not found! Create First")                
        return employees            