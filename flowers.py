"""User Input for Flower List: Prompt the user to enter names of flowers
and store them in a list. Have them enter the word "done" when done, and check for it.
Sorting and Searching: Sort the list, print on screen with a number next to the flower name,
 and allow the user to search for a specific flower. Print a message if the flower is found.
Accessing a Specific Flower: Ask the user for a number to access the corresponding flower. 
Handle errors for invalid inputs. 
(Note, our printout starts at 1, list indexes start at 0, adjust accordingly.
Exception Handling: Use try and except statements for ValueError and IndexError,
 and include a generic except statement.
 https://realpython.com/python-enumerate/ I used this to learn how to add numbers in front of the
 strings in the list a lot easier than i was making it for myself"""


def main():  # has a user make a list of flowers, "numbers" them then lets them access the list in 2 different was either by number or name
    flower_list = []
    gathering = True
    while gathering == True:  # "gathering" flowers for the list
        index = 1
        flower = input(
            "Please enter a flower or input 'Done' when you are done ").title()
        if flower == 'Done':  # cuts the while loop printing them with an index
            flower_list.sort()
            print(f"Here's the flower list")
            for plant in flower_list:
                print(index, plant)
                index += 1  # incrementing the index val for numbering the flowers
            gathering = False

        else:
            flower_list.append(flower)  # appends flower names to the list

    if gathering == False:  # starts the next section, asking for a number of flower to be searched
        querying_num = True
        while querying_num == True:
            try:
                query_num = input(
                    "Please enter the number of a flower to search or enter 'Done' ").title()
                if query_num == 'Done':  # cuts the while loop to move on to the name loop
                    querying_num = False

                else:
                    print(flower_list[int(query_num) - 1])
            except ValueError:  # catches val errors
                print(f"A Value error has occured \nPlease enter a number in numerics between 1 and {
                      len(flower_list)} or type 'done'")
            except IndexError:  # catches index errors
                print(f"Please enter a number in numerics between 1 and {
                      len(flower_list)}")
                continue
            except:  # catches unknown errors
                print(f"An error has occured \nPlease enter a number in numerics between 1 and {
                      len(flower_list)} or type 'done'")
                continue
    if querying_num == False:
        querying_name = True
        while querying_name == True:  # starts letting the user ask for names in the list
            query_name = input(
                "Please enter the name of a flower to search or type 'Done' ").title()
            if query_name == "Done":  # cuts the loop and also the main
                print(f"Here's the list one last time, {flower_list}")
                querying_name = False

            elif query_name in flower_list:  # checks to see if its in the list if not it displays so
                print(f"Yes, {query_name} is in the list")

            else:
                (f"No, {query_name} is not in the list")
                continue


main()
