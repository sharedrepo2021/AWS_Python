import json

if __name__ == "__main__":
    my_tuple = ('a','b','c','d','e',1,2)
    option_dict = {
        1: 'display my_tuple',
        2: 'Exit',
        3: 'Count the number of occurrences of an elements in a tuple',
        4: 'Access a specific element from the tuple',
        5: 'Display the length of the tuple',
        6: 'Show the datatype of the tuple',
        7: 'Delete the whole tuple',
        8: 'Search for a position of a specific element'
    }
    print(json.dumps(option_dict, indent=5))

    while True:
        try:
            i = int(input("Select an option of your choice: "))

            if i == 1:
                print(my_tuple)
            elif i == 2:
                print('Thank you')
                break
            elif i == 3:
                print(my_tuple.count(input(f"Enter an item from the tuple: ")))
            elif i == 4:
                print(my_tuple[int(input("Enter the index of the item you want to access: "))])
            elif i == 5:
                print(len(my_tuple))
            elif i == 6:
                print(type(my_tuple))
            elif i == 7:
                del my_tuple
            elif i == 8:
                x = input('Enter the item from the tuple to retrieve its index: ')

                print(my_tuple.index(int(x) if x.isnumeric() else x))
            else:
                print('Please select an available option from the list: ')


        except:
            print('Please enter a valid integer')