# Task 1: Create a Python program to model a vehicle rental system:

class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Make : {self.make}  \nModel : {self.model}"

class Car(Vehicle):
    def __init__(self, make, model,num_of_doors):
        super().__init__(make, model)
        self.num_of_doors = num_of_doors

    def additional_info(self):
        return f"Num Of Doors : {self.num_of_doors}"

class LuxuryCar(Car):
    def __init__(self, make, model, num_of_doors,features):
        super().__init__(make, model, num_of_doors)
        self.features = features

    def additional_info(self):
        return f"Features : {self.features}"

vehicle = Vehicle("Rolls Royce Ghost",2024)
car = Car("Lexus",2020,4)
luxurycar = LuxuryCar("Bugatti Chiron",2010,4,["Super Speed","Good Suspension","Comfortable"])

print(vehicle.display_info())
print(car.display_info())
print(car.additional_info())
print(luxurycar.display_info())
print(luxurycar.additional_info())


# Task 2: Create a python program to model a company's employee hierarchy.......

class Employee():
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def display_info(self):
        return f"Name : {self.name} \nPosition : {self.position}" 

class Manager(Employee):
    def __init__(self, name, position,department):
        super().__init__(name, position)
        self.department = department

    def additional_info(self):
        return f"Department : {self.department}"

class Worker(Employee):
    def __init__(self, name, position,hours_worked):
        super().__init__(name, position)
        self.hours_worked = hours_worked

    def additional_info(self):
        return f"Hours Worked : {self.hours_worked}"


employee = Employee("Uzair","Manager") 
manager = Manager("Asad","Manager","IT")
worker = Worker("Latif","Employee",50)

print(employee.display_info())
print(manager.display_info())
print(manager.additional_info())
print(worker.display_info())
print(worker.additional_info())