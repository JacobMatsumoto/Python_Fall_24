def main():
    valid = True
    while valid == True:
        valid_length = False
        valid_cap = False
        valid_lower = False  # setting flags
        valid_special = False
        valid_num = False
        user_pass = input(
            "Please enter a strong password, it should be 8-20 characters, include one upper and lower case letter,\none number and a special character ex.(!@#$%&*) ")
        if 8 <= len(user_pass) <= 20:
            valid_length = True
        else:
            print("Please enter a password with a length of 8-20")
            main()
        for character in user_pass:
            if character.isupper() == True:
                valid_cap = True  # checks upper, functioning
        if valid_cap == False:
            print("Please use an upper case letter")
            main()

        for character in user_pass:
            if character.islower() == True:
                valid_lower = True
        if valid_lower == False:  # checks lower, functioning
            print("please use a lower case letter")
            main()

        for character in user_pass:
            if character in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                valid_num = True
        if valid_num == False:  # checks num, functioning
            print("Please use a number")
            main()

        for character in user_pass:
            if character in ('!', '@''#', '$', '%', '&', '*'):
                valid_special = True
        if valid_special == False:  # checks special character, functioning
            print("Please use a special character ex.(!@#$%&*)")
            main()

        if valid_length and valid_cap and valid_lower and valid_special and valid_num == True:
            confirmed_password = input(
                "Please re-enter your password to confirm ")
            if confirmed_password == user_pass:
                print("Password confirmed")
                valid = False  # This wont break the loop for some reason, and I dont feel a break is appropriate
            else:
                print("Sorry re-enter your password")  # reseting works
                main()


main()
