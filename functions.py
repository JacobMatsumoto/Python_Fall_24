"""Start with Function Definitions:
Begin by defining two functions: square and circle.
Each function should take one parameter. For square, name the parameter side.
 For circle, name it radius.
Write the square Function:
Inside the square function, calculate the area of a square. Remember, the area of a 
square is the side length squared (side * side).
Use the print function to display the result. The output should be:
 "The area of the square is [result] square units." Replace [result] with the actual 
 calculated area.
Make sure to convert the numerical result to a string using str() 
before concatenating it with other strings.
Write the circle Function:
In the circle function, calculate the area of a circle using the formula: 
area = π * radius * radius. You can use 3.14 for π (pi).
Display the result using print, similar to the square function. The output should be: 
"The area of the circle is [result] square units."
Test Your Functions:
After defining both functions, test them by calling each one with a number of your choice.
For example, you can call square(4) and circle(5), but feel free to use any positive numbers.
Run Your Program:
Execute your program to see the output.
Ensure that the output correctly displays the areas for both the square and the circle
with the numbers you chose.
Tips:
Pay attention to the syntax, especially the indentation and the use of parentheses and colons.
Remember to use the print function to display the results.
Sample Results: (if you pass 4 and 5, you should use different numbers)"""
def square(side): #squares the variable side
    square = side * side
    print(f"The area is {square} square units")

side = 7
square(side)


def circle(radius):
    circle = 3.14 * radius
    print(f"The radius of the circle is {circle:.2f}")

radius = 10
circle(radius)

circle(9)
square(10)