height = float(input("Enter your height in cm:\n"))
weight = float(input("Enter your weight in kg:\n"))
BMI = ((weight/height/height) * 10000)
print(f"Your BMI index: {BMI}")
correct_weight = (18.5 <= (BMI) <25)
print(f"Correct weight: {correct_weight}")   