# Define the list of items needed to buy
needed_list = ["Apples", "Lettuce", "Bread", "Milk", "Peanut Butter"]

# Initialize a variable to keep track of items acquired
got_it = "ice cream"

# Loop until the user indicates they are done shopping
while got_it != "done":
    # Display the list of needed items
    for item in needed_list:
        print(item)

    # Prompt the user to enter the item they have acquired
    got_it = input(
        "\nPlease enter the item that you have gotten from the list:  ")

    # Check if the acquired item is in the list of needed items
    if got_it in needed_list:
        # If the item is found, remove it from the list
        needed_list.remove(got_it)

    # Check if all items have been acquired
    if len(needed_list) == 0:
        # If the list is empty, indicate that the shopping is complete
        print("You are done!")
        # Set the variable to 'done' to exit the loop
        got_it = "done"
