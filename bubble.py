"""Accept five names from the user.
Store these names in a list.
Sort the list using the Bubble Sort algorithm. 
Finally, reverse the sorted list using a Python list method. 
Requirements:
Your program should prompt the user to enter five names.
Use a loop to accept each name and append it to a list.
Implement the Bubble Sort algorithm to sort the list of names in ascending order.
Print the sorted list.
After sorting, use a Python list method to reverse the order of the list.
Print the final reversed list to the console."""
number = [1, 2, 3, 4, 5]
names = []
for name in number:
    name = input(f"Please enter name number {name} ")#prompt user for the names
    names.append(name)
for i in range(0, len(names)):
    names[i]=names[i].lower() #make names lowercase
swapped = True
while swapped: #bubble looping to sort the names
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            swapped = True
            names[i], names[i + 1] = names[i + 1], names[i]
print(names)
names.reverse()
print(names)