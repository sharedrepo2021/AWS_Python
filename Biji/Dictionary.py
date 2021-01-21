import json
if __name__ == "__main__":
    print('DICTIONARY PROCESSING')
    my_dictionary = {}
    option_dict = {
        1: 'Display the dictionary',
        2: 'Exit',
        3: 'Add a value',
        4: 'Remove elements from dictionary',
        5: 'Shows the value of a specified key',
        6: 'Display a list containing a tuple for each key value pair',
        7: 'Display all the keys of a dictionary',
        8: 'Displays list of all the values in the dictionary',
        9: 'Removes the last inserted key-value pair',
       10: 'Shows the value of the specified key',
       11: 'create a dictionary with specified keys',
       12: 'Updates the dictionary with the specified key-value pairs'

    }
    print(json.dumps(option_dict, indent=4))

    while True:
        i = int(input("Select an option : "))
        if i == 1:
            print(json.dumps(my_dictionary, indent=4))
        elif i == 2:
            break
        elif i == 3:
            x = input("Enter the key : ")
            y = input("Enter the value : ")
            my_dictionary[x] = y
        elif i == 4:
            x = input("Enter the value :")
            my_dictionary.pop(x)
        elif i == 5:
            x = input("Enter the key :")
            print(my_dictionary.get(x))
        elif i == 6:
            print(my_dictionary.items())
        elif i == 7:
            print(my_dictionary.keys())
        elif i == 8:
            print(my_dictionary.values())
        elif i == 9:
            my_dictionary.popitem()
            print("Deleted the last inserted key value pair")
        elif i == 10:
            x = input("Enter the key : ")
            y = input("Enter the value : ")
            print(my_dictionary.setdefault(x, y))
        elif i == 11:
            x = input("Enter the keys : ")
            y = input("Enter the value : ")
            print(my_dictionary.fromkeys(x, y))

        elif i == 12:
            x = input("Enter the key : ")
            y = input("Enter the value : ")
            my_dictionary.update({x: y})

        else:
            print("Please enter a valid option")