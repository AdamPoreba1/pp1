import random
computer_number = random.randint(1,6)
user_number = int(input("What number did computer roll?\n"))
fact_check = (computer_number == user_number)
print(fact_check)
print(f"The correct number was: {computer_number}")