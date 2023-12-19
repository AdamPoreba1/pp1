distance = int(input("Enter distance in km:"))
hours = int(input("Enter number of travel hours:"))
minutes = int(input("Enter number of travel minutes:"))


def avg_speed(distance,hours,minutes):
    minutes_to_hours = minutes / 60
    time = hours + minutes_to_hours
    speed = distance / time
    return speed


print(avg_speed(distance,hours,minutes))
