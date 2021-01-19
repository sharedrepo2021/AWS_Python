import json

if __name__ == "__main__":
    my_dict = {}
    option_dict = {
        1: 'display my_dict',
        2: 'Exit',
        3: 'Add an item to the dictionary',
        4: 'Remove specific item dictionary',
        5: 'Make a copy of the dictionary',
        6: 'Remove all items from the dictionary',
        7: 'Access a specific item from the dictionary',
        8: 'Display all items as a tuple',
        9: 'Display all keys',
        10: 'Remove the last item of the dictionary',
        11: 'Display all values',
        12: 'Search for a key',
        13: 'Insert a specific value for all dictionary keys',
        14: 'Search for a default value'
    }
    print(json.dumps(option_dict, indent=5))

    while True:
        try:
            i = int(input("Select an option of your choice: "))

            if i == 1:
                print(my_dict)
            elif i == 2:
                print('Thank you')
                break
            elif i == 3:
                my_dict.update({input('Please enter the key to be added in the dictionary: '):(input('Please enter the value for the corresponding key: '))})
            elif i == 4:
                my_dict.pop(input("Enter the key you want to remove: "))
            elif i == 5:
                new_dict = my_dict.copy()
                print(new_dict)
            elif i == 6:
                my_dict.clear()
            elif i == 7:
                print(my_dict.get(input("Enter the key to be extracted: ")))
            elif i == 8:
                print(my_dict.items())
            elif i == 9:
                print(my_dict.keys())
            elif i == 10:
                my_dict.popitem()
            elif i == 11:
                print(my_dict.values())
            elif i == 12:
                if input('Enter the key you want to look for: ') in my_dict:
                    print('It exists')
                else:
                    print('No such Key found')
            elif i == 13:
                my_dict = dict.fromkeys(my_dict.keys(),input('Enter the value you want to set as default: '))
            elif i == 14:
                my_dict.setdefault(input('Enter te key: '),input('Enter the value: '))


            else:
                print('Please select an available option from the dictionary: ')

        except:
            print('Please enter a valid integer')