"""Modify Artist List: Write a function to replace an artist in the top_artists list.
The function should ask the user for an index and a new artist name. 
Ensure your function catches and handles ValueError for invalid number conversion 
and IndexError for out-of-range indices.
General Error Handling: Modify your function to catch both 
ValueError and IndexError using a single except block. Provide a general error message 
like An input error occurred."""

# this all is just commented out old code for future reference,
# I made a dictionary for converting the numbers but then realized
# I can just do -1 to achieve the same thing easier and more efficiently.
# I just kept it because it's good reference if i do need to use a dictionary again
# dont know how I managed to not realize when writing the number conversion I was JUST doing -1
# def main():
#     num_conversion = {'1': 0, '2': 1, '3': 2, '4': 3,
#                       '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
#     top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
#                    "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
#     # Your code goes here
#     print(f"Here are the top 10 artists! {top_artists}")
#     finished = True
#     while finished == True:
#         try:
#             y_n = input(
#                 "Would you like to change the list? Enter 'Y' or 'N' ").upper()
#             if y_n in ('Y', 'YES'):
#                 artist_index = input(
#                     "Please choose between 1-10 which artist to replace ")
#                 new_artist = input("Enter a new artist's name please ").title()
#                 top_artists[num_conversion[artist_index]] = new_artist
#                 print(f"Here's an updated list! {top_artists}")
#             if y_n in ('N', 'NO'):
#                 print(f"Here is the finished top 10 {top_artists}")
#                 finished = False
#             else:
#                 print("Please ")
#                 continue
#         except KeyError:
#             print("An index error has occured")
#             continue
#         except:
#             print("An input error has occured")
#             continue


# main()
# so i originally used an

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    print(f"Here are the top 10 artists! {top_artists}")
    finished = True  # setting my while loop
    while finished == True:
        try:
            y_n = input(
                # main part of my loop tried to fool resistent it using .upper and letting 'yes' and 'y' work,
                "Would you like to change the list? Enter 'Y' or 'N' ").upper()
            if y_n in ('Y', 'YES'):
                artist_index = int(
                    input("Please choose between 1-10 which artist to replace "))
                # .title to make sure its formated right
                new_artist = input("Enter a new artist's name please ").title()
                # i re-did this because it's simpler and also way easier
                top_artists[artist_index-1] = new_artist
                # shows the new list updated
                print(f"Here's an updated list! {top_artists}")
            if y_n in ('N', 'NO'):
                print(f"Here is the finished top 10 {top_artists}")
                finished = False  # closing the while loop and printing the finished list
            else:
                print("Please enter 'Y' or 'N'")
                continue
        except ValueError:  # catches if they enter letters in the index int input
            print("An error has occured please enter a number between 1-10 in numerics")
            continue
        except IndexError:  # catches invalid index ie x<0 x>10
            print("An index error has occured please use 1-10")
        except:
            print("An input error has occured")
            continue
# sorry if my comments are misplaced, for some reason my code is jumping around and reformatting whenever I run or save programs
# it's a genuine headache for my ocd.


main()
