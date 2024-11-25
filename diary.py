
def main():

    # user input to file
    date = input("Enter the day's date ")
    event = input("What's one significant event from that day? ")
    memory = input(
        "Do you have something you'd like to remember from the date? ")
    happiness = input(
        "Overall what was your emotion for today? (ex: happy, sad etc) ")

    # opens file
    with open('diary.txt', 'a') as file:

        file.write(date + '\n' + event + '\n'
                   + memory + '\n' + happiness + '\n')  # writes to the file


main()
