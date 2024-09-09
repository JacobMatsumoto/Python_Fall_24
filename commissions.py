""" 
I am going to get the total dollar value of sales for the week,
add the number of sales from the user, Commision is based on
dollar value (under 1000, 5% 1000-2500, 7.5% over 2000 10%)
if they have a lot of low value sales the can still make extra
every 10 sales gives them a $25 bonus with a max of $250
"""
#Variables
name = input("Please enter the emploee's name ")
sales_count = int(input(f"How many sales did {name} have last week? " ))
sales_total = float(input(f"How much money did all the sales add up to? "))
#Logic
if sales_count < 10:
    bonus=0
elif sales_count < 20:
    bonus = 25
elif sales_count < 30:
    bonus = 50
elif sales_count < 40:
    bonus = 75
elif sales_count < 50:
    bonus = 100
elif sales_count < 60:
    bonus = 125
elif sales_count < 70:
    bonus = 150
elif sales_count < 80:
    bonus = 175
elif sales_count < 90:
    bonus = 200
elif sales_count < 100:
    bonus = 225
else:
    bonus = 250

if sales_total < 1000:
    commission =.05
elif sales_total < 2500:
    commission = .075
else: 
    commission = .10
print(f"{name} had a sales count of {sales_count}. They should get a bonus of {bonus:.2f}")
print(f"They had a total value of sales equal to ${sales_total}")
print(f"They earned a commission of ${sales_total*commission:.2f} with the bonus they earned a total of ${sales_total*commission+bonus:.2f}")