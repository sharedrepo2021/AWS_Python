import pandas as pd
import json

option_dict = {
    1: 'Create a simple Pandas series from a list',
    2: 'Return the first value of the Series',
    3: 'Create Labels',
    4: 'Access an item by referring to the label.',
    5: 'Create a simple Pandas Series from a dictionary',
    6: 'Create a Series using index and specify the items you want to see in the Series:',
    7: 'Create a DataFrame from two Series:',
    8:'use the loc attribute to return one or more specified row(s)',
    9:'Read CSV Files'

}
print(json.dumps(option_dict, indent=4))
while True:
    choice = int(input("Select an option : "))
    my_list = ["fd","sd","dewf"]
    myvar = pd.Series(my_list, index=["x", "y", "z"])
    calories = {"day1": 420, "day2": 380, "day3": 390}

    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    df=pd.DataFrame(data)
    if choice == 1:
        my_list.append(input('Enter the element you want to add : '))
        print(pd.Series(my_list))
    elif choice == 2:
         print(my_list[0])
    elif choice == 3:
        print(myvar)
    elif choice == 4:
        print(myvar['y'])
    elif choice == 5:
        mycal2 = pd.Series(calories)
        print(mycal2)
    elif choice == 6:
        mydickey= pd.Series(calories, index=["day1", "day2"])
        print(mydickey)
    elif choice == 7:
        print(pd.DataFrame(data))
    elif choice == 8:
        print(df.loc[0])
    elif choice == 9:
        dcsv = pd.read_csv('data.csv')
        print(df.to_string())

    else:
        print("Enter a valid option")
