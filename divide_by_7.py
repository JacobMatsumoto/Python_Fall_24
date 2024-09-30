"""Use a for loop to iterate through the range of numbers from 1 to 300.
Inside the loop, use an if statement to check if a number is divisible by 7. To do this, use the modulus operator (%) and compare the remainder with 0.
If a number is divisible by 7, print that number.
Ensure your program outputs each qualifying number on a separate line."""
for i in range (1, 300):
    if i % 7 == 0:
         print(i)