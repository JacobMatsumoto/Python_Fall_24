"""Objective: Develop a program to manage ticket sales for an event.
Context: You are in charge of ticket sales for a special event. 
The venue has 20 seats, each uniquely numbered from 1 to 20.
 Your task is to create a system that tracks 
 and updates the availability of seats as they are sold.
Assignment Steps:
Initialize the Seating List:
Create a list in your program representing the 20 seats.
 This list should initially include all seat numbers (1-20).
Display Available Seats:
Write code to display the list of available seats to the customer. 
This list should update as seats are sold.
Implement the Ticket Purchase Process:
Prompt the customer to select a seat by entering its number.
Include instructions in your prompt, indicating that the customer should enter '0' 
to finish their purchase.
Update Seat Availability:
Once a seat is selected, remove it from the list of available seats.
After each selection, display the updated list of available seats.
Continue this process until the customer enters '0', indicating they are done buying tickets.
Ensure User-Friendly Interaction:
Your program should handle inputs gracefully.
 If a customer selects a seat that doesn't exist or is already sold, 
 display a friendly message and prompt them to choose again."""
#TODO ^

tickets = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #Innitialise our list of availiable tickets
purchase = 5
while purchase != 0:
#setting a lot of ifs for different kinds of input from our users
    for ticket in tickets:
        print(f"\nPlease select an available ticket from the selection of availiable seats {tickets}")

        purchase = int(input("\nPlease enter the number of the ticket you wish to purchase. Or enter '0' to finish your purchase "))
        if purchase == 0: #Giving the customer an out after purchasing
             print("\nThank you for your patronage! Have a wonderful day!")
             break
        else:
            if purchase not in tickets:
             print("We're sorry! That is not an availiable seat, please select an availiable ticket")
        if purchase in tickets:
            confirm = int(input(f"if you would like to purchase seat {purchase} please enter a '0' "))
            if confirm == 0:
                print("\nThank you for your purchase!")
                tickets.remove(purchase)
            if confirm != 0:
                 print("\nSorry that you changed your mind!")
        if len(tickets) == 0:
                purchase = 0
                print("\nSorry the event is sold out!")