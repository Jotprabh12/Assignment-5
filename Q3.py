import math

def triangle_area(side1, side2, side3):
    # check if the combination of sides is possible
    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
        # calculate semi-perimeter
        s = (side1 + side2 + side3) / 2
        # calculate area using Heron's formula
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area
    else:
        return "The combination of sides is not possible for a triangle"

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

area = triangle_area(side1, side2, side3)

if type(area) == float:
    print("Area of the triangle: ", area)
else:
    print(area)