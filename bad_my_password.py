"""Set up your program in a main() function
Create a Python program that asks the user to input a password.
Ensure the password meets the following criteria:
Between 8 to 20 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Includes at least one number.
Includes at least one symbol from the set: !@#$%&*.
Use a while loop to keep asking for the password until all criteria are met.
Once a valid password is entered, prompt the user to enter it again for confirmation.
Use try-except blocks to handle any errors or exceptions that occur.
If the second password entry matches the first, display a success message. 
Otherwise, prompt the user to start the process again."""


def main():
    while True:
        user_pass = input(
            "Please enter a strong password, it should be 8-20 characters, include one upper and lower case letter,\none number and a special character ex.(!@#$%&*) ")
        try:
            if (8 <= len(user_pass) <= 20) == True:  # if for length
                if user_pass.isupper() == True:  # if for upper
                    if user_pass.islower() == True:  # if for lower
                        # if for number
                        if user_pass.find('1', '2', '3', '4', '5', '6', '7', '8', '9', '0') == True:
                            # if for special character
                            if user_pass.find('!', '@''#', '$', '%', '&', '*') == True:
                                re_enter = input(
                                    "Please re-enter your password ")
                                if re_enter == user_pass:
                                    print("Password set!")
                                    True
                            else:  # else for special character
                                print("Please use a special character ex.(!@#$%&*)")
                                main()
                        else:  # else for number
                            print("Please use a number")
                            main()
                    else:  # else for lower
                        print("please use a lower case letter")
                        main()
                else:  # else for upper
                    print("Please use an upper case letter")
                    main()
            else:  # else for length
                print("Please enter a password with a length of 8-20")
                main()

        except:
            main()


main()
