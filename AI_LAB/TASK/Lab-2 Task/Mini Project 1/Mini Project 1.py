

import random

class FizzBuzz:
    def __init__(self):
        print("Welcome to FizzBuzz Game.")

    def get_correct_answer(self, number):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz.")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz") 
        else:
            return number

    def play(self):
        
        while True:
            number = random.randint(1 , 50)
            print(f"\nNumber : {number}")
            user_input = input("Your Answer :").strip()

            if user_input.lower() == 'exit':
                print("Thanks for playing!")
                break 

            correct_answer = self.get_correct_answer(number)
            if user_input == correct_answer:
                print("Correct! next Number........") 
            else:
                print(f"Wrong! Correct Answer is {correct_answer}")
                break

game = FizzBuzz()
game.play()            
