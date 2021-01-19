import json
my_set = {"apple", "banana", "cherry"}
my_set1 = {1,2,3,'apple'}
option_dict = {
    1: 'display my_set',
    2: 'Exit',
    3: 'Add an element to the set',
    4: 'Remove all elements from the set',
    5: 'Make a copy of the set',
    6: 'Return a set containing the difference between two or more sets',
    7: 'Removes the items in this set that are also included in another, specified set',
    8: 'Remove the specified item',
    9: 'Returns a set, that is the intersection of two other sets',
    10: 'Removes the items in this set that are not present in other, specified set(s)',
    11: 'Returns whether two sets have a intersection or not',
    12: 'Returns whether another set contains this set or not',
    13: 'Returns whether this set contains another set or not',
    14: 'Removes an element from the set',
    15: 'Removes the specified element',
    16: 'Returns a set with the symmetric differences of two sets',
    17: 'inserts the symmetric differences from this set and another',
    18: 'Return a set containing the union of sets',
    19: 'Update the set with the union of this set and others'
}
print(json.dumps(option_dict, indent=5))

if __name__ == '__main__':

    try:
        while True:
            i = int(input('Please select an option from the above list: '))
            if i == 1:
                print(my_set)
            elif i == 2:
                break
            elif i == 3:
                print(my_set.add(input('Please provide the element you want to be entered in the set: ')))
            elif i == 4:
                print(my_set.clear())
            elif i == 5:
                new_set = my_set.copy()
                print(my_set1)
            elif i == 6:
                new_set = my_set.difference(my_set1)
                print(new_set)
            elif i == 7:
                my_set.difference_update(my_set1)
                print(my_set)
            elif i == 8:
                my_set1.discard(1)
                print(my_set1)
            elif i == 9:
                new_set = my_set.intersection(my_set1)
                print(new_set)
            elif i == 10:
                my_set.intersection_update(my_set1)
                print(my_set)
            elif i == 11:
                print(my_set.isdisjoint(my_set1))
            elif i == 12:
                print(my_set.issubset(my_set1))
            elif i == 13:
                print(my_set.issuperset(my_set1))
            elif i == 14:
                my_set.pop()
                print(my_set)
            elif i == 15:
                my_set.remove('cherry')
                print(my_set)
            elif i == 16:
                new_set = my_set.symmetric_difference(my_set1)
                print(new_set)
            elif i == 17:
                my_set.symmetric_difference_update(my_set1)
                print(my_set)
            elif i == 18:
                new_set = my_set.union(my_set1)
                print(new_set)
            elif i == 19:
                my_set.update(my_set1)
                print(my_set)
            else:
                print("Please select an appropriate option from the list")
    except Exception as e:
        print("Please select a proper integer", e)













    