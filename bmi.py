"""
This should be done inside of a main function. 
The conversion variables should be above main because they are global. 
Input:
Ask the user to enter their weight in pounds.
Ask the user to enter their height in inches.
Conversion to Metric:
These variables should be global and constant (at the top of the page and ALL CAPS) 
Convert weight from pounds to kilograms (1 pound = 0.453592 kilograms).
Convert height from inches to meters (1 inch = 0.0254 meters).
BMI Calculation:
Calculate the BMI using the formula: bmi = weight (kg) / (height (m) * height (m)).
Ensure the calculation is done using metric units.
BMI Categories:
Underweight: bmi < 18.5
Normal weight: 18.5 ≤ bmi < 24.9
Overweight: 25 ≤ bmi < 29.9
Obese: bmi ≥ 30
Output:
Display the calculated BMI with two decimal places.
Display the BMI category based on the calculated BMI.
"""

global METER_CONVR
METER_CONVR = .0254
global KG_CONVR
KG_CONVR = .453592
#^Globals

def weight_convr(lb):
    #converts lb-kg
    weight = lb * KG_CONVR
    return weight

def height_convr(inches):
    height = inches * METER_CONVR
    return height

def main():


    inches = int(input("Please enter your height in inches as a whole number  "))
    lb = int(input("Please enter your weight in pounds as a whole number  "))

    print(f"Your weight in kg is {weight_convr(lb):.2f}")

main()