"""Start by defining a function named factorial that takes one parameter,
 n, representing the number you're calculating the factorial for.
In your factorial function, first define the base case. The base case for our
 recursion will be when n is 1 or 0, because the factorial of 1 and 0 is 1.
For the recursive step, if n is greater than 1, the function should return n
 multiplied by a call to itself with n-1.
Create a main function. Inside this function, prompt the user to enter a 
non-negative integer. Use the int() function to convert the input to an integer.
Call the factorial function from your main function with the user's input as its 
argument, and print the result in a format like "The factorial of n is result."."""
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def main():
    n = int(input("Please enter a whole, positive number "))
    inp_n = factorial(n)
    print(f"{n}! is {inp_n:,.2f}")

main()
         
