import math
try:
    a = int(input('enter the first side: '))
    b = int(input('enter the second side: '))
    c = int(input('enter the third side: '))

    s = (a + b + c)/2
    area_triangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print('area of the triangle is =', area_triangle)
except:
    print('enter a valid integer')