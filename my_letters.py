"""Define a generator function two_letter_combinations that takes a list of characters 
as an argument.
Use nested loops within the generator function to iterate over the list of characters.
 In each iteration, concatenate two characters and use the yield statement to yield the 
 two-letter combination.
In the main method, call the generator function with a list of characters and iterate 
over the generator to print each combination. Create an original  5-letter list.
Include comments in your code to explain the logic behind the generator function and 
the use of the yield statement.
 """

alphabet = ['a', 'b', 'c', 'd', 'e']


def generator(a):  # generates the combinations, 'a' is the arguement i believe
    for letter in a:  # itterates through the list grabbing each one uniquely from combo
        for combo in a:  # itterates through the list grabbing each one uniquely/indipendantly from letter
            yield letter + combo  # puts them together


def main():
    result = list(generator(alphabet))
    print(result)


main()
