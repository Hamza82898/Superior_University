class Passenger:
    def __init__(self, name, age, passport_number):
        self.__name = name
        self.__age = age
        self.__passport_number = passport_number

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_passport_number(self):
        return self.__passport_number

    def display_info(self):
        print(f"Name: {self.__name} Age: {self.__age} Passport: {self.__passport_number}")

    def __eq__(self, other):
        return self.__passport_number == other.__passport_number


class EconomyClass(Passenger):
    def __init__(self, name, age, passport_number, seats_criteria):
        super().__init__(name, age, passport_number)
        self.seats_criteria = seats_criteria

    def display_info(self):
        super().display_info()
        print(f"Seats Criteria: {self.seats_criteria}")

    def get_seats_criteria(self):
        return self.seats_criteria


class BusinessClass(Passenger):
    def __init__(self, name, age, passport_number, luxury_seats):
        super().__init__(name, age, passport_number)
        self.luxury_seats = luxury_seats

    def display_info(self):
        super().display_info()
        print(f"Luxury Seats: {self.luxury_seats}")

    def get_luxury_seats(self):
        return self.luxury_seats


class FirstClass(Passenger):
    def __init__(self, name, age, passport_number, special_service):
        super().__init__(name, age, passport_number)
        self.special_service = special_service

    def display_info(self):
        super().display_info()
        print(f"Special Service: {self.special_service}")

    def get_special_service(self):
        return self.special_service