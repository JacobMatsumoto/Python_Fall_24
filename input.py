"""
    We are going to write a program that counts how many people order food, the
    cost of their order, add taxes, and a tip, then divide it by then number of
    people so they can split the check evenly.
"""

#Variables
cost = 0
count = 3
tax = .06
tip = .25
total = 0
cost_1 = float(input("How much was the first order?  "))
cost_2 = float(input("How much was the second order?  "))
cost_3 = float(input("How much was the third order?  "))

cost = cost + cost_1 + cost_2 + cost_3
total = (cost * tax) + (cost * tip) + cost

print(f"Your meal cost a total of: ${cost:.2f} including taxes of ${cost*tax:.2f} you should include a tip of ${cost*tip:.2f} resulting in a grand total of ${total:.2f}")