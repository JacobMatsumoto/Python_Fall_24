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


def main():
    flower_list = []
    gathering = True
    while gathering == True:
        index = 1
        flower = input(
            "Please enter a flower or input 'Done' when you are done ").title()
        if flower == 'Done':
            flower_list.sort()
            print(f"Here's the flower list")
            for plant in flower_list:
                print(index, plant)
                index += 1
            gathering = False

        else:
            flower_list.append(flower)

    if gathering == False:
        querying_num = True
        while querying_num == True:
            try:
                query_num = input(
                    "Please enter the number of a flower to search or enter 'Done' ").title()
                if query_num == 'Done':
                    querying_num = False

                else:
                    print(flower_list[int(query_num) - 1])
            except ValueError:
                print(f"A Value error has occured \nplease enter a number in numerics between 1 and {
                      len(flower_list)} or type 'done'")
            except IndexError:
                print(f"Please enter a number in numerics between 1 and {
                      len(flower_list)}")
                continue
    if querying_num == False:
        querying_name = True
        while querying_name == True:
            query_name = input(
                "Please enter the name of a flower to search or type 'Done' ").title()
            if query_name == "Done":
                print(f"Here's the list one last time, {flower_list}")
                querying_name = False

            elif query_name in flower_list:
                print(f"Yes, {query_name} is in the list")

            else:
                (f"No, {query_name} is not in the list")
                continue


main()
