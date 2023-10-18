first_person = input("Enter first person name: ")
first_person_age = float(input("Enter first person age:"))
second_person = input("Enter second person name: ")
second_person_age = float(input("Enter second person age: "))
if first_person_age >= 18 and second_person_age >=18:
    print(f"Both {first_person} and {second_person} are adults")