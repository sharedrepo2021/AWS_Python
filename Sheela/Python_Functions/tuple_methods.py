import json

if __name__ == "__main__":
    print('TUPLE PROCESSING')
    my_tuple = ()
    newtuple = ()

    option_dictupleoperation = {

        1: 'Display the Tuple',
        2: 'Add elements to the Tuple',
        3: 'Change Tuple Values',
        4: 'Unpack a Tuple',
        5: 'Join 2 Tuples',
        6: 'Multiply Tuples',
        7: 'Count the number of times the value appears in the tuple',
        8: 'Search and return Position for the first occurrence of the value',
        15: 'Exit'

    }
    print(json.dumps(option_dictupleoperation, indent=4))

    while True:
        i = int(input("Select an option : "))
        if i == 1:
            print(my_tuple)
        elif i == 2:
            y = list(my_tuple)
            y.append(input('Enter the element you want to add : '))
            my_tuple = tuple(y)
        elif i == 3:
            y = list(my_tuple)
            idx = int(input('Enter the index of the item : '))
            y[idx] = input("Enter the new item to be changed")
            my_tuple = tuple(y)
        elif i == 4:
          (first, *second) = my_tuple
          print("first :", first)
          print("second :", second)
        elif i == 5:
            y = list(newtuple)
            no_elements1 = input("Enter the number of elements to form new tuple ")
            for a in range(int(no_elements1)):
                y.append(input('Enter the element you want to add : '))
                newtuple = tuple(y)
            my_tuple = my_tuple + newtuple
        elif i == 6:
            my_tuple = my_tuple * 3
        elif i == 7:
            print(my_tuple.count(input("Enter the value to be counted :")))
        elif i == 8:
            print(my_tuple.index(input("Enter the value for which the position to be known :")))
        elif i == 15:
            break
        else:
            print("Please enter a valid option")