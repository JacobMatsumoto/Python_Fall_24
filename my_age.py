# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week

from datetime import datetime


def main():

    print("\n\n")
    try:
        today = datetime.today()
        birth_year = int(input("What year were you born?  (4 digits - 1972) "))
        month = int(
            input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output)

        delta = today - birthday
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.2425

        print(f'You are {delta_years} years old')

        # this calculates the days and converts it into months
        delta_months = delta.days // 30.41
        delta_weeks = delta.days // 7  # this does the same but for weeks

        print(f"You are {delta_months} months old")
        # these two print the results
        print(f"You are {delta_weeks} weeks old")

    except Exception as e:
        print(f"ooooops!!!:  {e}")
        main()


main()
