"""https://www.pythonforbeginners.com/basics/split-a-string-into-characters-in-python
I couldn't figure out fully how to do an objective 
so I used this to learn how to break the words into single letter strings, I also 
used your practice file from 10/9 to help me kinda mess with how these all work.
I had-
word = []
def spell_word():
    user_word = (input("Please enter a word "))
    for letter in user_word:
        word.append
-prior....... i was so close just forgot the (letter) somehow"""


word = []
def spell_word():#prompts user for a word, converts it to uppercase then appends each individual letter to the list "word"
    user_word = (input("Please enter a word "))
    user_word = user_word.upper()
    for letter in user_word:
        word.append(letter)
def main():#takes the users word and converts it into the nato equivilant.
    spell_word()
    nato_alphabet = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"}
    for value in word:
        print(nato_alphabet[value])
main()