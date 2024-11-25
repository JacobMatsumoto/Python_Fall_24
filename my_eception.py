"""Objective
Create a custom exception class to handle a specific error scenario in a Python program.

Task
Define a new exception class named NotNumericError that 
inherits from the base Exception class. This exception should be raised 
when a user inputs an invalid value in a simple input-validation program. 
Your program should prompt the user to enter a number and raise the InvalidInputError 
if the input is not a number.

Requirements
Implement a custom exception class NotNumericError.
Write a Python script that prompts the user to input a number.
Use a try-except-else-finally block:
The try block should contain the logic to check if the input is a number. (isnumeric() )
The except block should catch the InvalidInputError and print an error message.
The else block should print a confirmation message if the input is valid.
The finally block should print a message indicating the end of the program's execution.
Ensure the program gracefully handles the exception and continues to prompt 
the user until a valid number is entered. (call the program again)"""


class NotNumericError:
    def __init__(self, num, err="not a valid number"):
        self.num = num
        self.err = err
        super().__init__(self.err)

    def __str__(self):
        return f'{self.num} -> {self.err}'

    # def check_num(user_num):
    #     if not user_num.isnumeric():
    #         raise NotNumericError(user_num)
    #     print(f"Multipling {user_num}.")


def main():  # prompts user for a number and then handles errors if they occur
    try:
        user_in = input("Please enter a number ")
        if not user_in.isnumeric():
            raise NotNumericError(user_in)  # raises custom error
        user_num = int(user_in)
        print(f"Multipling {user_num}.")

    except NotNumericError as e:
        print(f"Error: {e}")

    except Exception as e:  # catches the unknown
        print(f"An error has occured{e}")

    else:
        print(f"{user_num} times 10 would be {user_num * 10} ")

    finally:
        print("Have a great day")


main()
