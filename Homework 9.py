def calculate_rectangle_perimeter():

    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))


    perimeter = 2 * (length + width)



    return perimeter
print(calculate_rectangle_perimeter())


print("\n_____________________________________________________________________________________")
def calculate_square_perimeter():

    side_length = float(input("Enter the side length of the square: "))


    perimeter = 4 * side_length


    return perimeter
print(calculate_square_perimeter())
print("\n_____________________________________________________________________________________")
#Third Task

def calculate_rectangle_area():

    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = length * width


    return area
print(calculate_rectangle_area())
print("\n_____________________________________________________________________________________")
#Fourth Task
def calculate_square_area2():

    side = float(input("Enter the length of the side of the square: "))

    area = side * side


    return area
print(calculate_square_area2())