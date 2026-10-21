marks = float(input("Enter your marks(1-100): "))
if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 1 and 100.") 
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")