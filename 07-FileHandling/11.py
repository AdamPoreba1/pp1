file = open('numbers.txt', 'r')
counter = 0
for number in file:
    counter = counter + int(number)

print(f"Sum is: {counter}")

file.close()