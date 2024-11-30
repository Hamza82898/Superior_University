class Flight:
    capacity = 10
    def __init__(self, flight_number, origin, destination):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Passenger {passenger.get_name()} successfully added to the flight.")
        else:
            print("Flight is full. Cannot add more passengers.")

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"Passenger {passenger.get_name()} removed from the flight.")
        else:
            print("Passenger not found in the list.")

    def display_flight_details(self):
        print(f"Flight {self.flight_number} from {self.origin} to {self.destination}")
        print(f"Capacity: {self.capacity}, Current Passengers: {len(self.passengers)}")
        for passenger in self.passengers:
            passenger.display_info()