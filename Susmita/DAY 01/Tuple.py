import json

if __name__ == "__main__":
    print('LIST PROCESSING')
    my_tuple = ('susmita', 'dipan', 'shreya', 'shresthaa', 'susmita')
    option_dict = {
        1: 'Display the tuple',
        2: 'Exit',
        3: 'Display the length of the tuple',
        4: 'Show the datatype of the tuple',
        5: 'Access a tuple element',
        6: 'Delete the whole tuple',
        7: 'Count the number of occurance of a certain element',
        8: 'Search for a position of a specific element'
    }
    print(json.dumps(option_dict, indent=4))

    while True:
        i = int(input("Select an option : "))
        if i == 1:
            print(my_tuple)
        elif i == 2:
            break

        elif i == 3:
            print(len(my_tuple))
        elif i == 4:
            print(type(my_tuple))
        elif i == 5:
            idx = int(input('Enter the index of the item : '))
            print(my_tuple[idx])
        elif i == 6:
            del my_tuple
        elif i == 7:
            ite = input("Enter the name of the item you want to search: ")
            print(my_tuple.count(ite))
        elif i == 8:
            print(my_tuple.index(input("Enter the name of the item you want to search: ")))
        else:
            print("Please enter a valid option")
