array = [34, 7, 19, 4, 21, 8]
even = 0
odd = 0
for i in array:
    if i % 2 == 0:
        even = even + 1
    elif i % 2 != 0:
        odd = odd + 1

print(even)
print(odd)