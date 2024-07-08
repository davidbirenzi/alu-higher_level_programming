#!/usr/bin/python3
"""
3-main.py

Main script to demonstrate the usage of the Rectangle class.
"""

Rectangle = __import__('3-rectangle').Rectangle

def main():
    # Create a Rectangle instance with width 2 and height 4
    my_rectangle = Rectangle(2, 4)
    
    # Print area and perimeter of the rectangle
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    # Print string and formal representation of the rectangle
    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    # Change width to 10 and height to 3
    my_rectangle.width = 10
    my_rectangle.height = 3
    
    # Print updated rectangle string and formal representation
    print(my_rectangle)
    print(repr(my_rectangle))

if __name__ == "__main__":
    main()

