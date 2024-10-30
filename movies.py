"""In this assignment, you will create a Python program that collects book titles from a user. 
Your program should use a while loop to prompt the user to enter a total of 10 book titles. 
Follow these steps to complete your assignment:

Set Up the Main Function: Write your program inside a main function. 
This is where your while loop will be implemented.
Collect Book Titles: Use a while loop to ask the customer to enter 10 book titles. 
Store these titles in a list.
Ensure proper capitalization: Use the title function to make sure the 
first letter is capitalized before storing into the list.
Create a Sorted List: Once all titles are collected, save them to a new list named sorted.
 This list should contain the titles in alphabetical order.
Display the Titles: Use a for loop to print each title from the sorted list on a separate line."""


def main():  # prompts 10 titles from the user, title()s them then will append them to the user list, which then gets sorted
    user_list = []
    while len(user_list) != 10:  # ensures length of 10
        # prompts the user to enter a name and automatically .titles() it
        movie = input("Please enter a movie title ").title()
        user_list.append(movie)  # added to user list
    # sorts and transfers the list to sorted_list
    sorted_list = sorted(user_list)
    for item in sorted_list:
        print(item)


main()
