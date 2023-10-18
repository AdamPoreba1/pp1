height_cm = int(input("Enter your height in centimiters:\n"))
height_feet = int(height_cm // 30.48) # 30.48=1 feet
rest = int(height_cm % 30.48)
height_inches = round(rest/2.54)
print(f"I am {height_cm} cm tall, i.e. {height_feet} feet and {height_inches}")