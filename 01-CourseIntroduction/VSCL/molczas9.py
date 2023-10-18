total_questions = int(input("What is the number of tasks: "))
correct_answers = int(input("Number of correctly completed tasks: "))
percentage = (correct_answers / total_questions) * 100
if percentage >= 50:
    print("Test passed") 
