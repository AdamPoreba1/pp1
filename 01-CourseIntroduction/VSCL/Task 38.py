phone_number = (input("Enter your phone number:\n"))
formatted_phone_number = (f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}")
print(f"Phone number: {formatted_phone_number}")