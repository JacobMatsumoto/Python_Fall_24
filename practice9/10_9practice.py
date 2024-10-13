def main():
    week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    for day in week:
        print(day)
    length = len(week)
    print(f"There are {length} days in a week")

main()
#Below is the use of dictionaries 
# create a secret code using dictionaries
def main():
    code = {"A": "❤", "B": "😃", "C": "😖", "D": "🤣"}

    # access using keys
    print(code["A"])

    # using get()
    print(code.get("B", "😎"))

    # iterate through all keys
    for key in code:
        print(key, code[key])

    # iterate through key value pairs
    for key, value in code.items():
        print(key, value)


main()
