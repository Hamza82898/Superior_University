from passenger import *


class Reservation:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def show_available_flights(self):
        print("Available Flights:")
        for flight in self.flights:
            flight.display_flight_details()

    def book_ticket(self, flight, passenger):
        if passenger is not None:
            flight.add_passenger(passenger)
        else:
            print("No passenger to add.")

    def cancel_ticket(self, flight, passenger):
        flight.remove_passenger(passenger)


def create_info_passenger():
    class_type = input("Enter class type (Economy/Business/First Class/Exit): ").lower()
    if class_type not in ['economy','business','first class','exit']:
        print("Invalid Class Type!")
    if class_type == 'economy':
        name = input("Enter passenger name: ")
        age = input("Enter passenger age: ")
        passport_number = input("Enter passenger passport number: ")
        seats_criteria = input("Enter passenger seat criteria (window/comforts): ")
        return EconomyClass(name, int(age), passport_number, seats_criteria)
    elif class_type == 'business':
        name = input("Enter passenger name: ")
        age = input("Enter passenger age: ")
        passport_number = input("Enter passenger passport number: ")
        luxury_seats = input("Enter luxury seats (front seat/comforts seat): ")
        return BusinessClass(name, int(age), passport_number, luxury_seats)
    elif class_type == 'first class':
        name = input("Enter passenger name: ")
        age = input("Enter passenger age: ")
        passport_number = input("Enter passenger passport number: ")
        special_service = input("Enter special service (Special_treatment,cabin) ")
        return FirstClass(name, int(age), passport_number, special_service)
    elif class_type == 'exit':
        print("Exiting the program. Thanks for visiting our airline.")
        return None
    else:
        print("Invalid class type")
        return create_info_passenger()