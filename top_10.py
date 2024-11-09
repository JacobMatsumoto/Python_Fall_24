"""Modify Artist List: Write a function to replace an artist in the top_artists list.
The function should ask the user for an index and a new artist name. 
Ensure your function catches and handles ValueError for invalid number conversion 
and IndexError for out-of-range indices.
General Error Handling: Modify your function to catch both 
ValueError and IndexError using a single except block. Provide a general error message 
like An input error occurred."""


def main():
    num_conversion = {'1': 0, '2': 1, '3': 2, '4': 3,
                      '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    print(f"Here are the top 10 artists! {top_artists}")
    finished = True
    while finished == True:
        try:
            y_n = input(
                "Would you like to change the list? Enter 'Y' or 'N' ").upper()
            if y_n in ('Y', 'YES'):
                artist_index = input(
                    "Please choose between 1-10 which artist to replace ")
                new_artist = input("Enter a new artist's name please ").title()
                top_artists[num_conversion[artist_index]] = new_artist
                print(f"Here's an updated list! {top_artists}")
            if y_n in ('N', 'NO'):
                print(f"Here is the finished top 10 {top_artists}")
                finished = False
            else:
                continue
        except KeyError:
            print("An index error has occured")
            continue
        except:
            print("An input error has occured")
            continue


main()
