import json

if __name__ == "__main__":
    print('LIST PROCESSING')
    my_dict = {}
    option_dict = {
        1: 'Display the dict',
        2: 'Exit',
        3: 'Add elements to you dict',
        4: 'Remove element from you dict',
        5: 'Search for a key',
        6: 'Display the keys',
        7: 'Display the values',
        8: 'Update the key value',
        9: 'Delete the last key and value pair',
        10: 'Delete the whole dictionary',
        11: 'Clear the directory',
        12: 'Insert a specific value for all dictionary keys',
        13: 'Search for a default value',
        14: 'Copy the same dictionary and print it'
    }
    print(json.dumps(option_dict, indent=4))

    while True:
        i = int(input("Select an option : "))
        if i == 1:
            print(json.dumps(my_dict, indent=4))
        elif i == 2:
            break
        elif i == 3:
            x = input('Enter the key : ')
            my_dict[x] = input('Enter value : ')
        elif i == 4:
            my_dict.pop(input('Enter the element you want to remove : '))
        elif i == 5:
            print(my_dict.get(input('Enter the key name for search : ')))

        elif i == 6:
            print(my_dict.keys())
        elif i == 7:
            print(my_dict.values())
        elif i == 8:
            my_dict.update({input('Enter key name'): input('Enter the value')})
        elif i == 9:
            my_dict.popitem()
        elif i == 10:
            del my_dict
        elif i == 11:
            my_dict.clear()
        elif i == 12:
            my_dict = dict.fromkeys(my_dict.keys(), input('Enter the value: '))
        elif i == 13:
            l = my_dict.setdefault(input('Enter the key'), input('Enter the value'))
            print(l + ' is not here')
        elif i == 14:
            my_dictcopy = my_dict.copy()
            print(json.dumps(my_dictcopy, indent=4))

        else:
            print("Please enter a valid option")
