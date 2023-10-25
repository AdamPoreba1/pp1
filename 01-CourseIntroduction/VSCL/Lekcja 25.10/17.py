def different(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n1!=n3:
        return True
    else:
        return False



n1 = input("Enter first number:\n")
n2 = input("Enter second number:\n")
n3 = input("Enter third number:\n")
if different(n1,n2,n3):
    print(f"Numbers {n1}, {n2} and {n3} are different")
else:
    print((f"Numbers {n1}, {n2} and {n3} are the same"))
