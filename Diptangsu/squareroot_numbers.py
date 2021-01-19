import math
try:
    first_number = int(input('enter the first number: '))
    square_root = math.sqrt(first_number)
    print('summation =', square_root)
except:
    print('enter a valid integer')