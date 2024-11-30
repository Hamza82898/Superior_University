from passenger import EconomyClass
from passenger import BusinessClass
from passenger import FirstClass
from flight import Flight

import csv



class FileHandling:
    def save_passenger_details(passengers, filename = "passenger.csv"):
        with open(filename, mode="w", newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Passport Number", "Class type", "Additional Info"])
            for passenger in passengers:
                if isinstance(passenger,EconomyClass):
                    class_type = "Economy"
                    additional_info = passenger.get_seats_criteria()
                elif isinstance(passenger,BusinessClass):
                    class_type = "Business"
                    additional_info = passenger.get_luxury_seats()
                elif isinstance(passenger,FirstClass):
                    class_type = "First"
                    additional_info = passenger.get_special_service()
                else:
                    continue
                writer.writerow([passenger.get_name(), passenger.get_age(), passenger.get_passport_number(), class_type, additional_info])

    def read_passenger(filename = "passenger.csv"):
        passengers = []
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row.get("Name", "Unknown")
                age = int(row.get("Age", 0))
                passport_number = row.get("Passport Number", "Unknown")
                class_type = row.get("Class Type", "Any")
                additional_info  = row.get("Additional Info", "")
                # name, age, passport_number, class_type, additional_info = row

                if class_type == "Economy":
                    passengers.append(EconomyClass(name, age, passport_number, additional_info))
                elif class_type == "Business":
                    passengers.append(BusinessClass(name, age, passport_number, additional_info))
                elif class_type == "First":
                    passengers.append(FirstClass(name, age, passport_number, additional_info)) 
            return passengers

    def save_flight_info(flights, filename = "flight.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Flight Number", "Origin", "Destination", "Capacity", "Passengers Passport"])
            for flight in flights:
                passenger_passports = [p.get_passport_number() for p in flight.passengers]
                writer.writerow([flight.flight_number, flight.origin, flight.destination, flight.capacity, ",".join(passenger_passports)])

    def read_flights(filename = "flight.csv", passengers = None):
        flights = []
        passengers = passengers or  []
        passengers_dict = {p.get_passport_number(): p for p in passengers}

        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                flight_number = row.get("Flight Number", "Unknown") 
                origin = row.get("Origin", "Unknown")
                destination = row.get("Destination", "Unknown")
                capacity = int(row.get("Capacity", 0))
                passenger_passport = row.get("Passenger Passport", "").split(",")

                flight = Flight(flight_number, origin, destination,capacity)
                for passport in passenger_passport:
                    if passport in passengers_dict:
                        flight.add_passenger(passengers_dict[passport])
                flights.append(flight)
        return flights                
  
