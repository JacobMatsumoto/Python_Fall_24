"""In this exercise, you will practice using logical operators (and, or, not) in Python.
 Your task is to create a program that prompts 
the user for two integer inputs and then demonstrates the use of these operators.

User Input: Start by asking the user to input two distinct integers. 
Logical Operators: Implement six different logical comparisons using the input integers.
 Include two examples for each of the following operators:
and
or
not
Display Results: For each comparison, print both the logical statement and its result.
Guidelines for Logical Comparisons:
Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
Try to use comparisons that could yield different results based on user input.
Sample Output: Here's an example of what your program's output might look like:"""

int_1 = int(input("Please enter an integer for variable a "))
int_2 = int(input("Please enter another integer for variable b "))
if int_1 > 0 and int_2 > 0:
    print("Both a and b are greater than 0")
elif int_1 < 0 or int < 0:
    print("One or both numbers are not greater than 0")
if not int_1 > int_2:
    print("a is not greater than b")
else:
    print("a is greater than b")
if int_1 % 2 == 0 or int_2 % 2 == 0:
    print("a and/or b is even")
else:
    print("Neither a nor b are even")
if int_1 + int_2 > 100:
    print("The sum of a and b is greater than 100")
else:
    print("The sum of a and b is not greater than 100")
if int_1 < 0 or int_2 < 0:
    print("One or both numbers are negative")
else:
    print("Both numbers are possitive")