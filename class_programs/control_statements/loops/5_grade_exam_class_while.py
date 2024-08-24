# WAP to find the class of a student passed in the exam based on percentage
total_no_of_students = int(input("Enter the number of students in the class: "))
i = 1
while i <= total_no_of_students:
    percentage_of_marks = float(input(f"Enter the percentage of marks scored in the exam by student-{i}: "))
    if percentage_of_marks >= 70 and percentage_of_marks <= 100:
        print(f"Student-{i} passed in the distinction")
    elif percentage_of_marks >= 60 and percentage_of_marks < 70:
        print(f"Student-{i} passed in the First class")
    elif percentage_of_marks >= 50 and percentage_of_marks < 60:
        print(f"Student-{i} passed in the Second class")
    elif percentage_of_marks >= 35 and percentage_of_marks < 50:
        print(f"Student-{i} passed in the Third class")
    elif percentage_of_marks >= 0 and percentage_of_marks < 35:
        print(f"Student-{i} successfully failed in the exam")
    else:
        print(f"Student-{i} has entered in the invalid marks")
    i = i + 1
print("End of the program")
