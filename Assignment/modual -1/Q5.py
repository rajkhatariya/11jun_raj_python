# Q-5 How does the Python code structure work?
# Import section
import math

# Global variable
PI = 3.14

# Function definition
def area_of_circle(radius):
    return PI * radius ** 2

# Main program
if __name__ == "__main__":
    r = float(input("Enter the radius: "))
    area = area_of_circle(r)
    print("Area of circle:", area)
