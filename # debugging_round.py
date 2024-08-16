# debugging_round.py

import math

class Rectangle:
    def __init__(self, lenght, bredth):
        self.lenght = lenght
        self.bredth = bredth

    def calculate_area(self):
        return self.lenght * self.bredth

    def calculate_perimeter(self):
        return 2 * (self.lenght + self.bredth)

    def calculate_diagonal(self):
        return (self.lenght ** 2 + self.bredth ** 2) ** 0.5

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side

def main():
    lenght = int(input("Enter the lenght of the rectangle: "))
    bredth = int(input("Enter the bredth of the rectangle: "))

    rectangle = Rectangle(lenght, bredth)
    area = rectangle.calculate_area()
    perimeter = rectangle.calculate_perimeter()
    diagonal = rectangle.calculate_diagonal()

    print("The area of the rectangle is: " ,area)
    print("The perimeter of the rectangle is: " ,perimeter)
    print("The diagonal of the rectangle is: " ,diagonal)

    radius = int(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    area = circle.calculate_area()
    circumference = circle.calculate_circumference()

    print("The area of the circle is: " ,area)
    print("The circumference of the circle is: ", circumference)

    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    triangle = Triangle(base, height)
    area = triangle.calculate_area()

    print("The area of the triangle is: " ,area)

    side = int(input("Enter the side of the square: "))
    square = Square(side)
    area = square.calculate_area()
    perimeter = square.calculate_perimeter()

    print("The area of the square is: " ,area)
    print("The perimeter of the square is: " ,perimeter)

    if area > 100:
        print("The area is greater than 100")
    elif area < 50:
        print("The area is less than 50")
    else:
        print("The area is between 50 and 100")

    try:
        file = open("output.txt", "w")
        file.write("The area of the rectangle is: " ,area)
        file.write("The perimeter of the rectangle is: " ,perimeter)
        file.write("The diagonal of the rectangle is: " ,diagonal)
        file.write("The area of the circle is: " ,area)
        file.write("The circumference of the circle is: " ,circumference)
        file.write("The area of the triangle is: " ,area)
        file.write("The area of the square is: " ,area)
        file.write("The perimeter of the square is: " ,perimeter)
    except:
        print("Error writing to file")

    list_of_areas = [10, 20, 30, 40, 50]
    list_of_perimeters = [100, 200, 300, 400, 500]
    list_of_diagonals = [10.0, 20.0, 30.0, 40.0, 50.0]

    for i in range(5):
        print("Area at index ", i, "is: " , list_of_areas[i])
        print("Perimeter at index " ,i, "is: " ,list_of_perimeters[i])
        print("Diagonal at index " ,i ,"is: " ,list_of_diagonals[i])

    dict_of_shapes = {"rectangle": {"area": area, "perimeter": perimeter, "diagonal": diagonal},
                      "circle": {"area": area, "circumference": circumference},
                      "triangle": {"area": area},
                      "square": {"area": area, "perimeter": perimeter}}
    print("The area of the rectangle is: " ,dict_of_shapes["rectangle"]["area"])
    print("The perimeter of the rectangle is: ", dict_of_shapes["rectangle"]["perimter"])
    print("The diagonal of the rectangle is: " ,dict_of_shapes["rectangle"]["diagnol"])
    print("The area of the circle is: " ,dict_of_shapes["circle"]["area"])
    print("The circumference of the circle is: " ,dict_of_shapes["circle"]["circumfernce"])
    print("The area of the triangle is: " ,dict_of_shapes["triangle"]["area"])
    print("The area of the square is: " ,dict_of_shapes["square"]["area"])
    print("The perimeter of the square is: " ,dict_of_shapes["square"]["perimter"])

    list_of_shapes = [rectangle, circle, triangle, square]
    for shape in list_of_shapes:
        if isinstance(shape, Rectangle):
            print("Rectangle: area = " ,shape.calculate_area() ," perimeter = " ,shape.calculate_perimeter() ," diagonal = " ,shape.calculate_diagonal())
        elif isinstance(shape, Circle):
            print("Circle: area = " ,shape.calculate_area() ,"circumference = " ,shape.calculate_circumference())
        elif isinstance(shape, Triangle):
            print("Triangle: area = " ,shape.calculate_area())
        elif isinstance(shape, Square):
            print("Square: area = ", shape.calculate_area() ,", perimeter = ", shape.calculate_perimeter())

if __name__ == "__main__":
    main()