import random

list_01 = [13, 14, 15]
list_02 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(15):

    print('{} X {} =\t\t\t{} X {} =\t\t\t{} X {} =\t\t\t'.
          format(random.choices(list_01)[0], random.choices(list_02)[0],
                 random.choices(list_01)[0], random.choices(list_02)[0],
                 random.choices(list_01)[0], random.choices(list_02)[0]))