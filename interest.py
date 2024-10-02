"""Define the function calculate_interest with the appropriate parameters.
Inside the function, apply the formula to calculate the simple interest.
Ensure that the function returns the calculated interest and stores it in a 
variable named result. 
Print the variable, in a user-friendly string, formatted. 
print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
                at an interest rate of {interest_rate}% over a period of \
                {investment_time} years is: ${calculated_interest:,.2f}")

the \ is a symbol you can use to split a string over multiple lines

The {principal_amount:,.2f} format specifier formats the principal amount as a 
floating-point number with two decimal places, and includes commas as thousand separators.
The {calculated_interest:,.2f} does the same for the calculated interest.
Test your function with different values to ensure it works correctly."""

def calculate_interest(principle, rate, time):
    interest = (principle*rate*time) / 100
    return interest

inp_principle = int(input("Please enter the principle amount "))
inp_rate = int(input("Please enter the interest rate as a whole number "))
inp_time = int(input("Please enter the investment time in whole years "))
# principle = inp_principle
# rate = inp_rate
# time = inp_time ----> this is how i coded it originally
# calculated_interest = calculate_interest(principle, rate, time)
calculated_interest = calculate_interest(principle = inp_principle, rate = inp_rate, time = inp_time)
print(f"With a innitial principle amount of ${inp_principle:,.2f} at a yearly rate of {inp_rate}% for {inp_time} years \nwill give you an interest of ${calculated_interest:,.2f}")

