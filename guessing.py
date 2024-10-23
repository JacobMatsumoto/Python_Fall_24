"""Import the random module and use it to generate a random number between 1 and 100.
Put the rest of the code in the main function; use try and except statements. 
The except statement should look for ValueError
Write a while loop that allows the user to enter a guess for the number.
Inside the loop, use the abs() function to calculate the absolute difference 
between the guess and the actual number.
Based on this difference, provide the following feedback to the user:
If the difference is within 5, print "Very Hot".
If the difference is within 15, print "Hot".
If the difference is within 25, print "Cool".
If the difference is more than 25, print "Cold".
The loop should continue until the user guesses the correct number.
Make sure to call the main function!"""


import random
def main():
   try:
      num = random.randrange(0, 101)
      user_guess = 0
        #print(num) -test
      while user_guess!=num:
        user_guess = int(input("Please enter a guess for a number between 1-100! "))
        if user_guess == num:
          print(f"Thats correct the number was {num}")
        elif abs(user_guess - num) <= 5:
          print("Hot!")
        elif abs(user_guess - num) <= 15:
          print("Warm")
        elif abs(user_guess - num) <= 25:
          print("Cool")
        elif abs(user_guess - num) >= 25:
           print("Cold")
        elif user_guess == num:
          print(f"Thats correct the number was {num}")
   except ValueError:
    print("Please enter a valid number between 1-100 in numerics")
    main()


main()
