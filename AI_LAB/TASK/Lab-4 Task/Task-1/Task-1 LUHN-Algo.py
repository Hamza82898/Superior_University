# ....LUHN Algorithm....

def Luhn_Algorithm(card_number):
    card_number = card_number.replace(" ", "")

    if not card_number.isdigit():
        return False
    
    digits = [int(digit) for digit in card_number]
    digits.reverse()

    for i in range(len(digits)):
        if i % 2 == 1:
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

    total_sum = sum(digits)
    return total_sum % 10 == 0
  
card_number = input("Enter a card number :")       
if Luhn_Algorithm(card_number):
    print("Card Is Valid.")
else:
    print("Card Is Invalid!")    