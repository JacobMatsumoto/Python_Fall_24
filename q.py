"""Write the program "99 Bottles of Beer on the Wall" using a while loop. 
Be mindful to change the word 'bottles' to 'bottle' when you are down to the last one. 
You need to do the full 99 bottles the sample shows the last 3 verses.
"""
count = 99 #defining our count
while count > 1:
    print(f"{count} bottles of beer on the wall " f"\n{count} bottles of beer" "\nTake one down pass it around")
    count -= 1 #incrementing it to count down
    if count == 1: #insurance for grammar on 1 bottle
         print(f"{count} bottle of beer on the wall")
    else:print(f"{count} bottles of beer on the wall")
    if count == 1:
         print(f"{count} bottle of beer on the wall"f"\n{count} bottle of beer""\nTake it down pass it around" "\nNo more bottles of beer on the wall!")