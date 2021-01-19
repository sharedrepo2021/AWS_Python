import json

if __name__ == "__main__":
    my_list = []
    option_dict = {
        1: 'display my_list',
        2: 'Exit',
        3: 'Add an element to the list',
        4: 'Remove all elements from the list',
        5: 'Make a copy of the list',
        6: 'Count the number of occurrences of an elements in a list',
        7: 'Extend the list',
        8: 'Access a specific element from the list',
        9: 'Add an item to a specific position in the list',
        10: 'Remove an item from a specific position in a list',
        11: 'Remove an item with a specific value in the list',
        12: 'Reverse the order of a list',
        13: 'Sort the list',
        14: 'Display the length of the list'
    }
    print(json.dumps(option_dict, indent=5))

    while True:
        try:
            i = int(input("Select an option of your choice: "))

            if i == 1:
                print(my_list)
            elif i == 2:
                print('Thank you')
                break
            elif i == 3:
                my_list.append(input('Please enter the item to be added in the list: '))
            elif i == 4:
                my_list.clear()
            elif i == 5:
                new_list = my_list.copy()
                print(new_list)
            elif i == 6:
                print(my_list.count(input(f"Enter an item from the list: ")))
            elif i == 7:
                my_list.extend(input("Enter the new iterables to be added: "))
            elif i == 8:
                print(my_list[int(input("Enter the index of the item you want to access: "))])
            elif i == 9:
                my_list.insert(int(input("Enter the position of item you want to insert: ")),(input("Enter the item you want to insert: ")))
            elif i == 10:
                my_list.pop(int(input("Enter the index of the item you want to remove: ")))
            elif i == 11:
                my_list.remove(input("Please enter the item to be removed from the list: "))
            elif i == 12:
                my_list.reverse()
            elif i == 13:
                sort_type = input("Do you want to sort the list in reverse? (Y/N): ")
                if sort_type == 'Y':
                    my_list.sort(reverse=True)
                else:
                    my_list.sort()
            elif i == 14:
                print(len(my_list))
            else:
                print('Please select an available option from the list: ')


        except:
            print('Please enter a valid integer')
