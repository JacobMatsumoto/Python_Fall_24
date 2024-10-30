"""_summary_
    programming the song bingo
    """


def main():
    dog = "Bingo"
    dog = list(dog)
    bingo = ''.join(dog)
    my_num = 4
    for n in range(0, 6):
        print(f"There was a farmer who had a dog")
        print(f"And {bingo} was his nameo")
        for num in range(0, 3):
            for letter in bingo:
                print(letter.upper(), end=" ")
            print()
        print(f"And {bingo} was his nameo")
        dog[my_num] = "🐶"
        my_num -= 1
        bingo = ''.join(dog)


main()
