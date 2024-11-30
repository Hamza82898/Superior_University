from reservation import *
from flight import *
from reservation import *
from filehandling import *
import os

def main_menu():
    reservation_system = Reservation()
    while True:
        print("\n<<<<<Airline Reservation System>>>>>")
        print("1- Add Flight")
        print("2- Display Available Flights")
        print("3- Book Ticket")
        print("4- Cancel Ticket")
        print("5- Read Passenger Details")
        print("6- Read Flight Details")
        print("7- Exit")

        choice = input("Enter Your choice:")

        if choice == "1":
            flight_number = input("Enter flight no: ")
            origin = input("Enter your origin: ")
            destination = input("Enter your destination: ")
            new_flight = Flight(flight_number,origin,destination)
            reservation_system.add_flight(new_flight)
            print(f"Flight {flight_number} Added Successfully.")

            if reservation_system.flights:
                FileHandling.save_flight_info(reservation_system.flights)
                print("Flight Saved.") 
            else:
                print("Flight Not Saved!")

        elif choice == "2":
            reservation_system.show_available_flights()
        
        elif choice == "3":
            if not reservation_system.flights:
                print("No Flight Available.Create First")
                continue
            reservation_system.show_available_flights()
            flight_number = input("Enter Flight No: ")   
            flight = next((f for f in reservation_system.flights if f.flight_number == flight_number) , None)
            if not flight:
                print("Invalid Flight No!")
                continue
            Passenger = create_info_passenger()
            if Passenger:
                reservation_system.book_ticket(flight,Passenger)

            all_passengers = []
            for flight in reservation_system.flights:
                all_passengers.extend(flight.passengers)
            if all_passengers:
                FileHandling.save_passenger_details(all_passengers)
                print("Passenger Saved Successfully.") 
            else:
                print("No passenger save.")    
        
        elif choice == "4":
            reservation_system.show_available_flights()
            flight_number = input("Enter flight no to cancel ticket.")
            flight = next((f for f in reservation_system.flights if f.flight_number == flight_number) , None)
            passport_number = input("Enter your Passport NO: ") 
            passenger = next((p for p in flight.passengers if p.get_passport_number() == passport_number) , None)  
            if not flight:
                print("Invalid FLight No!")
                continue
            if not reservation_system.flights:
                print("No Flight.Add First")
                continue
            if passenger:
                reservation_system.cancel_ticket(flight,passenger)
            else:
                print("Passenger not found!!!") 

        elif choice == "5":
            os.startfile("passenger.csv")

        elif choice == "6":
           os.startfile("flight.csv")

        elif choice == "7":
            print("Exit.Thank You! To Visit Airline Reservation System........")
            break

        else:
            print("Invalid Choice!")

main_menu()