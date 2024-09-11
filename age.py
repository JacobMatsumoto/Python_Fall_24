"""Write a Python program that uses if else statements and:

Ask the user for their age.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount (65).
Print all the results on the screen."""
#asking user for information
age = int(input("What is your age?  "))
#using said information to calculate if they are old enough for certain things
if age < 18:
    print("You aren't old enough to drive or vote")
else:print("You are old enough to drive and vote")
if age < 21:
    print("You aren't old enough to buy alchohol")
else:print("You are old enough to buy alchohol")
if age < 65:
    print("You aren't elegible for senior discounts")
else:print("You are elegible for senior discounts")