# Value of celsius entered by the user
Celsius = float(input("Enter temperature in Celsius:\n"))
# Celsius converting to Kelvin
Kelvin = (Celsius + 273.15)
# Celsius converting to Fahrenheit
Fahrenheit = (9/5 * Celsius + 32)
# Display the temperature in Kelvin and Fahrenheit
print(f"If the temperature in Celsius is {Celsius}, then the temperature in Kelvin is: {Kelvin} ")
print(f"If the temperature in Celsius is {Celsius}, then the temperature in Fahrenheit is: {Fahrenheit} ")