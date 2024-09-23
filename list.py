"""Welcome to your Python assignment! This task will help you practice working with lists, 
user input, and basic calculations. Follow the steps below:
Create a List: Start by creating a list named days that includes all seven days of the week.
Initialize an Empty List: Create an empty list called steps. 
This will store the number of steps taken each day.
User Input: Using a loop, ask the user to enter the number of steps they took for each day, 
based on your days list. For example, "How many steps did you take on Monday?"
Store Steps: Append the user's input (number of steps) to the steps list for each day.
Display Daily Steps: Show the user the steps recorded for each day.
Total Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Create a variable named average to calculate the average steps taken. 
Use the formula: average = round(total / len(steps)). Display the average steps.
Remember to test your program to ensure it runs correctly."""

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
steps=[]
mon=int(input("How man steps did you take on Monday? "))
steps.append(mon)
tues=int(input("How man steps did you take on Tuesday? "))
steps.append(tues)
wed=int(input("How man steps did you take on Wednesday? "))
steps.append(wed)
thurs=int(input("How man steps did you take on Thursday? "))
steps.append(thurs)
fri=int(input("How man steps did you take on Friday? "))
steps.append(fri)
sat=int(input("How man steps did you take on Saturday? "))
steps.append(sat)
sun=int(input("How man steps did you take on Sunday? " ))
steps.append(sun)
total=(mon+tues+wed+thurs+fri+sat+sun)
# average=round(total_steps/7) what i originally wrote before rereading instructions
for i in range(len(days)):
    day= days[i]
    step=steps[i]
    print(f"You walked {step} on {day}")


average = round(total / len(steps))
print(f"You waled a total of {total} steps with an average of {average} of steps per day")