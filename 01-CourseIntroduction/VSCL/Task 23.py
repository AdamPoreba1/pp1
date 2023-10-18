import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
triangle_circumference = (a+b+c)
s = ((a+b+c)/2)
triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"Triangle area:{triangle_area}")
print(f"Triangle circumference: {triangle_circumference}")
