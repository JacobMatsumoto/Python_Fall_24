"""Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
Identify Potential Errors: Consider errors that might occur with non-numeric input.
Add Exception Handling: Implement try and except blocks to catch a ValueError. 
Handle incorrect data types with an error message and reprompt."""


# Simple Python program to calculate the square of a number

def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError: #This knocks bad data down to an error message, and reprompts them to enter a valid number
        print(f"Sorry but {number} is not a numerical whole number")
        square_number()

square_number()

    