car_registration = input("Enter vehicle registration number:\n")
is_car_cracow = car_registration.startswith("KR") or car_registration.startswith("KK")
print(f"Car from Cracow: {is_car_cracow}")