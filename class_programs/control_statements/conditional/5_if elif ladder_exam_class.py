# WAP to find the class of a student passed in the exam based on percentage
percentage_of_marks = float(input("Enter the percentage of marks scored in the exam: "))
if percentage_of_marks >= 70 and percentage_of_marks <=100:
    print("Student passed in the distinction")
elif percentage_of_marks >= 60 and percentage_of_marks <70:
    print("Student passed in the First class")
elif percentage_of_marks >= 50 and percentage_of_marks <60:
    print("Student passed in the Second class")
elif percentage_of_marks >= 35 and percentage_of_marks <50:
    print("Student passed in the Third class")
elif percentage_of_marks >= 0 and percentage_of_marks <35:
    print("Student successfully failed in the exam")
else:
    print("Student has entered in the invalid marks")
print("End of the program")
