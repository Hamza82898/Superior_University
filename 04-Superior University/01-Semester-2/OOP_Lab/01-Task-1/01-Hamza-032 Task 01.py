def is_prime(number):
    if number <= 1:
        return False
     
    for i in range(2,number):
        if number % i==0:
            return False
    return True
    
while True:
    user_input=input("Enter number(or type'Exit' to stop.):")
    if user_input=="exit":
        print("Exit")
        break

    number=int(user_input)
    if is_prime(number):
        print(f"The {number} is prime number.")

    else:
        print(f"The {number} is not prime number.")    