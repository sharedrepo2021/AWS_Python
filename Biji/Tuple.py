import json

if __name__ == "__main__":
    print('TUPLE PROCESSING')
    my_tuple = ()
    option_dict = {
        1: 'Display the tuple',
        2: 'Exit',
        3: 'Add values to the tuple',
        4: 'Display the number of times a specified value occurs in a tuple',
        5: 'Delete tuple',
        6: 'Display the position of a specified value',
        7: 'Update value of a tuple at a specified position'

    }
    print(json.dumps(option_dict, indent=4))

    while True:
        i = int(input("Select an option : "))
        if i == 1:
            print(my_tuple)
        elif i == 2:
            break
        elif i == 3:
            y = input("Enter the value : ")
            lst = list(my_tuple)
            lst.append(y)
            print(lst)
            my_tuple = tuple(lst)
            print(my_tuple)

        elif i == 4:
            y = input("Enter the value : ")
            print(my_tuple.count(y))

        elif i == 5:

            del my_tuple
        elif i == 6:
            x = input("Enter the value")
            print(my_tuple.index(x))
        elif i == 7:
            x = int(input("Enter the index of the value to be changed:"))
            y = input("Enter new value:")
            lst = list(my_tuple)
            lst[x] = y
            my_tuple = tuple(lst)
            print(my_tuple)
        else:
            print("Please enter a valid option")
