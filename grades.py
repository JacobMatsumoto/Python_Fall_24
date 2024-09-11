"""Accept a numeric grade from the user and display a letter grade. 
The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F
Check to see if the number given is between 0 and 100.  """
#acquiring the relevant information from the user
name = input("What is the students name?  ")
grade = int(input("What score did the student achieve?  "))
#calculating the grade
if grade < 60:
    score = 'F'
elif grade < 70:
    score = 'D'
elif grade < 80:
    score = 'C'
elif grade < 90:
    score = 'B'
else: score = 'A'

if grade < 90:
    print(f"{name} got a {score}")
else: print(f"{name} got an {score}")
#Grammar is important