distance = int(input("Enter distance in km:"))
hours = int(input("Enter number of travel hours:"))
minutes = int(input("Enter number of travel minutes:"))

speed = lambda a,b,c: distance/(hours + (minutes/60))
print(speed(distance,hours,minutes))