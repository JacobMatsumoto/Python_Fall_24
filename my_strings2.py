def main():
    # Example string
    example_string = "Hello, Python programmers!"


# TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for letter in example_string:
        print(letter)
# TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    ascii_num1 = []  # innitialized the list
    for letter in example_string:  # iterate through the list
        ascii_value = ord(letter)  # obtain values
        ascii_num1.append(ascii_value)  # add them to the list
    ascii_num1.sort()  # order them
    print(ascii_num1[0])


# TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    ascii_num2 = []
    for letter in example_string:
        ascii_value = ord(letter)
        # copied my work from ascii_num1 and just reversed it
        ascii_num2.append(ascii_value)
    ascii_num2.sort()
    ascii_num2.reverse()  # only change
    print(ascii_num2[0])
# TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    o_index = example_string.find('o')
    print(o_index)
# TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    letters_list1 = []
    for letter in example_string:
        letters_list1.append(letter)
    print(letters_list1)

# TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    o_count = example_string.count('o')
    print(o_count)


main()
