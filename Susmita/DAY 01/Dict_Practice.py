import json

user_dict = {}
while True:
    string = input('Enter some key/value pairs ("quit" to quit): ')
    if string == 'quit':
            break

    elif string.count(' ') != 1:
            print('Malformed input!')
            continue

    key, value = string.split()

    user_dict[key] = value
print(user_dict)
user_dict1 = {}

while True:
    key = input("Enter key name:: ")
    if key:
        user_dict1[key] = input("Enter value:: ")
    else:
        break

print(user_dict1)
dict3 = {**user_dict, **user_dict1}
# user_dict = user_dict.update(user_dict1)
print(dict3)
# new_dict = {}
search_key = input("Enter the key you want to search:: ")
for key in dict3.keys():
    if key == search_key:
        print("Key is valid!")


search_key_delete = input("Enter the key you want to delete:: ")
dict3.pop(search_key_delete)
print(dict3)







