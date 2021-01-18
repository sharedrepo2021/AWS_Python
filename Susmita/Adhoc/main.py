import json

my_list = ['a', 'b', 'c', 'd']

option_dict = {
    1: 'Append a letter',
    2: 'Copy a letter',
    3: 'Delete a letter',
    4: 'Reverse the list',
    5: 'Add a element in a special position'

}
print(json.dumps(option_dict, indent=4))
i = int(input("What you want to do : "))

if i == 1:

    b = input("Enter a letter: ")
    my_list.append(b)
    print(my_list)
elif i == 2:
    b = my_list.copy()
    print(b)
elif i == 3:
    b = input("Enter a letter you want to delete: ")
    my_list.remove(b)
    print(my_list)
elif i == 4:
    my_list.reverse()
    print(my_list)
else:
    b = input("Enter a letter you want to insert in 2nd position: ")
    my_list.insert(1, b)
    print(my_list)

