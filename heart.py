"""Define Time Slots:
Create a list named time_slots with different times of the day, 
such as "Morning", "Midday", "Afternoon", "Evening".
User Input for Heart Rate:
Use a loop to iterate over each time slot. For each time slot, use the input() 
function to ask the user to enter their heart rate (in beats per minute). 
Convert this input to an integer.
Storing Heart Rate Data:
Create an empty list named heart_rates. For each time slot, 
append a sublist to heart_rates that contains the time slot and the corresponding heart rate.
Calculate Average Heart Rate:
Initialize a variable to keep track of the total heart rate. Use a loop to 
add up the heart rate recorded at each time slot. Calculate and print the average heart rate
 at the end."""
total = 0 #innitializzing later varriables
average = 0
time_of_day = ["Morning", "Midday", "Afternoon", "Evening"] #starting lists
heart_rate = []
for time in time_of_day:
    rate = (input(f"Enter your heart rate for {time}: " )) #getting user input for heart rate to use in calcs
    heart_rate.append([time, rate])

print(heart_rate)

for i in range(4):
    time = heart_rate[i][0]
    rate = heart_rate[i][1]
    total += int(rate)
    print(f"In the {time} your heart rate was {rate}")

average = total / 4
print (f"You had an average heart rate of {average:.0f} today") #I got stuck here for a little bit for forgetting the f in ":.0f" found it when rubber duck methoding funny enough!