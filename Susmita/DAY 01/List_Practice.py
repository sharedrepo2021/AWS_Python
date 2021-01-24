list1 = []
list2 = []
length = int(input("Enter the length of the list1:: "))
for l in range(length):
    name = input("Enter whatever you want :: ")
    list1.append(name)

print(list1)
for l in range(length):
    name = input("Enter whatever you want :: ")
    list2.append(name)

print(list2)
dict1 = {}
dict2 = {}
dict1['list1'] = list1
dict2['list2'] = list2
dict3 = {**dict1, **dict2}
print(dict3)

