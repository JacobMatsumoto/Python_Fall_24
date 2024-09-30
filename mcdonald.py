"""Select a Song: Choose a song that is well-known and suitable for a classroom setting. 
Avoid any song with inappropriate or offensive content.
Identify Variables: Determine at least 8 different variables that the user will 
provide to customize the song. These could include names, adjectives, nouns, places, etc.
Write the Function:
Define a function named custom_song that takes at least 8 parameters 
corresponding to the variables you've identified.
Use f-strings to incorporate these parameters into the song's lyrics.
Ensure the function prints the customized song lyrics.
Collect User Input:
Write code to collect user input for each of the 8 variables.
Use clear and descriptive prompts to guide the user.
Call the Function:
Call the custom_song function with the user inputs as named arguments.
Ensure the order of arguments matches the parameters in your function definition"""

def song(adjective, name, place, animal1, sound1, animal2, sound2, animal3, sound3):
    print(f"{adjective} {name} had a {place} E-I-E-I-O")
    print(f"And on that {place} he had a {animal1} E-I-E-I-O")
    print(f"with a {sound1} {sound1} here and a {sound1} {sound1} there \nhere a {sound1} there a {sound1} everywhere a {sound1} {sound1}")
    print(f"{adjective} {name} had a {place} E-I-E-I-O")
    print(f"{adjective} {name} had a {place} E-I-E-I-O")
    print(f"And on that {place} he had a {animal2} E-I-E-I-O")
    print(f"with a {sound2} {sound2} here and a {sound2} {sound2} there \nhere a {sound2} there a {sound2} everywhere a {sound2} {sound2}")
    print(f"{adjective} {name} had a {place} E-I-E-I-O")
    print(f"{adjective} {name} had a {place} E-I-E-I-O")
    print(f"And on that {place} he had a {animal3} E-I-E-I-O")
    print(f"with a {sound3} {sound3} here and a {sound3} {sound3} there \nhere a {sound3} there a {sound3} everywhere a {sound3} {sound3}")
    print(f"{adjective} {name} had a {place} E-I-E-I-O")

adjective_inp = input("Please enter an adjective ")
name_inp = input("Please enter a name ")
place_inp = input("Please enter a place ")
animal1_inp = input("Please enter an animal ")
sound1_inp = input("Please enter a noise the animal might make ")
animal2_inp = input("Please enter a different animal ")
sound2_inp = input("Please enter another noise it may make ")
animal3_inp = input("Please enter another different animal ")
sound3_inp = input("Please enter another noise it may make ")

song(adjective=adjective_inp, name=name_inp, place=place_inp, animal1=animal1_inp, sound1=sound1_inp, animal2=animal2_inp, sound2=sound2_inp, animal3=animal3_inp, sound3=sound3_inp)