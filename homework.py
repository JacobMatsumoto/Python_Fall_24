"""Requirements:
Design a Python program that prompts users to enter their total budget and amounts for different spending categories 
Housing (rent or mortgage),Utilities,Groceries,Transportation,Health Care,Personal Care,
Clothing,Debt,Calculate the percentage of the total budget spent in each category.
Display the results in a user-friendly format, clearly showing the budget breakdown. (use f strings)
Ensure your code is well-commented to explain the functionality of different sections.
"""
#Getting variables through input from users
budget = int(input("What is your budget?  "))
housing = int(input("How much do you spend on housing?  "))
utilities = int(input("How much do you spend on utilites?  "))
groceries = int(input("How much do you spend on groceries?  "))
transportation = int(input("How much do you spend on transportation?  "))
health_care = int(input("How much do you spend on health care?  "))
personal_care = int(input("How much do you spend on personal care?  "))
clothing = int(input("How much do you spend on clothing?  "))
debt = int(input("How much do you spend on debts?  "))
#Using said variables to calculate budget utilization
housing_percent = housing/budget*100
utilities_percent = utilities/budget*100
groceries_percent = groceries/budget*100
transportation_percent = transportation/budget*100
health_care_percent = health_care/budget*100
personal_care_percent = personal_care/budget*100
clothing_percent = clothing/budget*100
debt_percent = debt/budget*100
#add it all together to find their total utilization
budget_utilitization = housing_percent+utilities_percent+groceries_percent+transportation_percent+health_care_percent+personal_care_percent+clothing_percent+debt_percent
print(f"You are spending {housing_percent}% of your budget on housing, {utilities_percent}% of your budget on utilities,")
print(f"{groceries_percent}% of your budget on groceries,  {transportation_percent}% of your budget on transportation,")
print(f" {health_care_percent}% of your budget on health care, {personal_care_percent}% of your budget on personal care,")
print(f" {clothing_percent}% of your budget on clothing, and finally {debt_percent}% of your budget on debts,")
print(f" You use {budget_utilitization}% of your total budget!")