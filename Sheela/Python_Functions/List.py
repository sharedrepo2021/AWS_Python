import json
import pandas

if __name__ == "__main__":
    print('LIST PROCESSING')
    my_list = []
    option_dict = {
        1: 'Display the list',
        2: 'Exit',
        3: 'Add elements to you list',
        4: 'Remove element from you list',
        5: 'Extend the list',
        6: 'Display the length of the list',
        7: 'Show the datatype of the list',
        8: 'Access a list element',
        9: 'Change an item within the list',
        10: 'Insert an item at a specific position within the list',
        11: 'Delete an item from a specific position within the list',
        12: 'Sort the items of the list',
        13: 'Reverse the items of the list',
        14: 'Clear the list'
    }
    print(json.dumps(option_dict, indent=4))

    while True:
        i = int(input("Select an option : "))
        if i == 1:
            print(my_list)
        elif i == 2:
            break
        elif i == 3:
            my_list.append(input('Enter the element you want to add : '))
        elif i == 4:
            my_list.remove(input('Enter the element you want to remove : '))
        elif i == 5:
            my_list.extend(input('Enter the list you want to add : '))
        elif i == 6:
            print(len(my_list))
        elif i == 7:
            print(type(my_list))
        elif i == 8:
            print(my_list[int(input('Enter the index of the item : '))])
        elif i == 9:
            idx = int(input('Enter the index of the item : '))
            my_list[idx] = input('Enter the item : ')
        elif i == 10:
            my_list.insert(int(input('Enter the index of the item : ')), input('Enter the item : '))
        elif i == 11:
            my_list.pop(int(input('Enter the index of the item : ')))
        elif i == 12:
            my_list.sort()
        elif i == 13:
            my_list.reverse()
        elif i == 14:
            my_list.clear()
        else:
            print("Please enter a valid option")