import json
if __name__ == "__main__":
    print('DICTIONARY PROCESSING')
    my_dictionary = {}
    option_dict = {
        1: 'Display the dictionary',
        2: 'Add Key and Values to the Dictionary',
        3: 'Keys : Return all  keys in dictionary',
        4: 'Values :  all  values in dictionary',
        5: 'Items : Returns the  dictionarys key-value pairs',
        6: 'Get a value for a specific key',
        7: 'Set default value if key doesnt exisit else return value',
        8: 'Generate keys with default value 0',
        9: 'Remove a specified item from the dictionary',
        10: 'Remove the last item in the dictionary',
        11: 'Create copy of the specified dictionary',
        12: 'Clear the Dictionary',
        13: 'Exit'
    }
    print(json.dumps(option_dict, indent=4))

    while True:
        i = int(input("Select an option : "))
        if i == 1:
            print(json.dumps(my_dictionary, indent=4))
        elif i == 2:
            my_dictionary.update({input("Enter the Key : "): input("Enter the value : ")})
        elif i == 3:
            print("Prints Keys :", my_dictionary.keys())
        elif i == 4:
            print("Print Values :", my_dictionary.values())
        elif i == 5:
            print("Print Values :", my_dictionary.items())
        elif i == 6:
            value =  my_dictionary.get(input("Enter the Key to get the value"))
            print("Value for the key is : ", value)
        elif i == 7:
            x = my_dictionary.setdefault(input("Enter the key to search :"), input("Enter default value if not found :"))
            print("Returned Value", x)
        elif i == 8:
            no_elements1 = input("number of keys needs to be generated")
            no_key = input("Enter the key name")
            y = 0
            keygeneration = []
            for a in range(int(no_elements1)):
                keygene = no_key + str(a)
                keygeneration.append(keygene)
            keygenerated = tuple(keygeneration)
            dic_keys = dict.fromkeys(keygenerated, y)
            print("dic_keys generated :", dic_keys)
        elif i == 9:
            my_dictionary.pop(input("Enter the key to be removed"))
        elif i == 10:
            my_dictionary.popitem()
        elif i == 11:
            copydictionary = my_dictionary.copy()
            print("Copied Dictionary")
            print(json.dumps(copydictionary, indent=4))
        elif i == 12:
            my_dictionary.clear()
        elif i == 13:
            break
        else:
            print("Please enter a valid option")