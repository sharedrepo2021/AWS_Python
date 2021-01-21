import json

if __name__ == "__main__":
    print('LIST PROCESSING')
    my_list = []
    newlist = []

    def newListfunc():
        no_elements1 = input("Enter the number of elements to form new list ")
        for a in range(int(no_elements1)):
             newlist.append(input("Enter the value for the list"))
        return newlist

    option_dictListoperation = {
        1: 'Display the list',
        2: 'Display number of items in the list',
        3: 'Add elements to you list',
        4: 'Remove element from you list',
        5: 'Extend the list',
        6: 'Show the datatype of the list',
        7: 'Access a list element',
        8: 'Change an item within the list',
        9: 'Insert an item at a specific position within the list',
        10: 'Delete an item from a specific position within the list',
        11: 'Sort the items of the list',
        12: 'Reverse the items of the list',
        13: 'Copy a list into a exisiting list',
        14: 'Clear the list',
        15: 'Exit'
    }
    print(json.dumps(option_dictListoperation, indent=4))

    while True:
        i = int(input("Select an option : "))
        if i == 1:
            print(my_list)
        elif i == 2:
            print(len(my_list))
        elif i == 3:
            my_list.append(input('Enter the element you want to add : '))
        elif i == 4:
            my_list.remove(input('Enter the element you want to remove : '))
        elif i == 5:
            my_list.extend(newListfunc())
        elif i == 6:
            print(type(my_list))
        elif i == 7:
            print(my_list[int(input('Enter the index of the item : '))])
        elif i == 8:
            idx = int(input('Enter the index of the item : '))
            my_list[idx] = input('Enter the item : ')
        elif i == 9:
            my_list.insert(int(input('Enter the index of the item : ')), input('Enter the item : '))
        elif i == 10:
            my_list.pop(int(input('Enter the index of the item : ')))
        elif i == 11:
            my_list.sort()
        elif i == 12:
            my_list.reverse()
        elif i == 13:
            newlist = newListfunc()
            my_list = newlist.copy()
        elif i == 14:
            my_list.clear()
        elif i == 15:
            break
        else:
            print("Please enter a valid option")