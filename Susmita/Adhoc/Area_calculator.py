import json


class Area:
    def __init__(self):
        pass

    def circle(self, radius):
        print("The area of circle is : {}".format(22/7 * radius * radius))

    def square(self, length):
         print("The area of square is : {}".format(length * length))

    def rectangle(self, length, width):
         print("The area of rectangle is : {}".format(length * width))

    def triangle(self, base, height):
         print("The area of triangle is : {}".format(1/2 * base * height))


if __name__ == '__main__':

    option_dict = {
        1: 'Area of a circle',
        2: 'Area of a square',
        3: 'Area of a rectangle',
        4: 'Area of a triangle',
        5: 'Exit'

    }
    print(json.dumps(option_dict, indent=4))

    while True:
        i = int(input("Select a main menu option : "))
        if i == 1:
            r = int(input("Enter the radius of the circle: "))
            c1 = Area()
            c1.circle(r)

        elif i == 2:
            l = int(input("Enter the length of the square: "))
            c1 = Area()
            c1.square(l)
        elif i == 3:
            l = int(input("Enter the length of the rectangle: "))
            w = int(input('Enter the width of the rectangle: '))
            c1 = Area()
            c1.rectangle(l, w)

        elif i == 4:
            l = int(input("Enter the height of the triangle: "))
            w = int(input('Enter the base of the triangle: '))
            c1 = Area()
            c1.triangle(l, w)

        else:
            break

