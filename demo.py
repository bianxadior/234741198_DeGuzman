# Used to access mathematical functions and import the math module
import math

# Codes for color to add design
RED = '\033[91m'
ORANGE = '\033[38;5;208m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
VIOLET = '\033[38;5;165m'
PINK = '\033[38;5;211m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Title
print("Welcome to Area Calculator Pro Max Fully Paid")

# List of the available choices
def display_choices():
  print("Choose a shape you want to calculate the area:")
  print("\033[96m1. Square□" + RESET)
  print("\033[38;5;208m2. Rectangle▭" + RESET)
  print("\033[93m3. Triangle△" + RESET)
  print("\033[92m4. Trapezoid" + RESET)
  print("\033[38;5;165m5. Hexagon⬡" + RESET)
  print("\033[38;5;211m6. Octagon⯃" + RESET)
  print("\033[94m7. Circle〇" + RESET)
  print("\033[91m8. Exit the caculator✖️" + RESET)
  print("=====================")

# Functions for the formulas of the shapes
def squareArea(side):
    return side * side

def rectangleArea(length, width):
    return length * width

def triangleArea(base, height):
    return 1/2 * base * height

def trapezoidArea(base1, base2, height):
    return 1/2 * (base1 + base2) * height

def hexagonArea(side):
    return (3 * math.sqrt(3) * side ** 2) / 2

def octagonArea(side):
    return 2 * (1 + math.sqrt(2)) * side * side

def circleArea(radius):
    return math.pi * radius * radius

# Used so that users should only put numbers
def numberOnly(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


# Input and Printing
while True:
    display_choices()
    option = input("Enter your chosen command(1-8): ")

# Area of SQUARE
    if option == '1':
        print("You have selected command 1\033[96m(Square□)"+ RESET)
        side = numberOnly("Enter the side length of the square: ")
        area = squareArea(side)
        print(f"The area of the square is: {area}")
        print("========================")

# Area of RECTANGLE
    elif option == '2':
        print("You have selected command 2\033[38;5;208m(Rectangle▭)" + RESET)
        length = numberOnly("Enter the length of the rectangle: ")
        width = numberOnly("Enter the width of the rectangle: ")
        area = rectangleArea(length, width)
        print(f"The area of the rectangle is: {area}")
        print("========================")

# Area of TRIANGLE
    elif option == '3':
        print("You have selected command 3\033[93m(Triangle△)" + RESET)
        base = numberOnly("Enter the base of the triangle: ")
        height = numberOnly("Enter the height of the triangle: ")
        area = triangleArea(base, height)
        print(f"The area of the triangle is: {area}")
        print("========================")

# Area of TRAPEZOID
    elif option == '4':
        print("You have selected command 4\033[93m(Trapezoid)" + RESET)
        base1 = numberOnly("Enter the first base of the trapezoid: ")
        base2 = numberOnly("Enter the second base of the trapezoid: ")
        height = numberOnly("Enter the height of the trapezoid: ")
        area = trapezoidArea(base1, base2, height)
        print(f"The area of the trapezoid is: {area}")
        print("========================")

# Area of HEXAGON
    elif option == '5':
        print("You have selected command 5\033[38;5;165m(Hexagon⬡)" + RESET)
        side = numberOnly("Enter the side length of the hexagon: ")
        area = hexagonArea(side)
        print(f"The area of the hexagon is: {area}")
        print("========================")

# Area of OCTAGON
    elif option == '6':
        print("You have selected command 6\033[38;5;211m(Octagon⯃)" + RESET)
        side = numberOnly("Enter the side length of the octagon: ")
        area = octagonArea(side)
        print(f"The area of the octagon is: {area}")
        print("========================")

# Area of CIRCLE
    elif option == '7':
        print("You have selected command 7\033[94m(Circle〇)" + RESET)
        radius = numberOnly("Enter the radius of the circle: ")
        area = circleArea(radius)
        print(f"The area of the circle is: {area}")
        print("========================")

    elif option == '8':
        print("\033[91mYou are now exiting the program. Thank You!" + RESET)
        break

    else:
        print("Please enter a number from 1 to 8 only.")

