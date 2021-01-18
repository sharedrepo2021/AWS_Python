import json

x = input('Enter a text: ')
option_dict = {
    1: 'Convert to uppercase',
    2: 'Convert to lowercase',
    3: 'Remove extra whitespaces',
    4: 'Capitalize sentence',
    5: 'Casefold',
    6: 'Print length',
    7: 'Check if lower',
    8: 'Check if upper'
}
print(json.dumps(option_dict, indent=4))

i = int(input("Select an option :"))
if i == 1:
    x = x.upper()
    print(x)
elif i == 2:
    x = x.lower()
    print(x)
elif i == 3:
    x = " ".join(x.split())
    print(x)
elif i == 4:
    x = x.capitalize()
    print(x)
elif i == 5:
    x = x.casefold()
    print(x)
elif i == 6:
    x = len(x)
    print(x)
elif i == 7:
    if x.islower():
        print("Sentence in lowercase")
    else:
        print("Sentence not in lowercase")
elif i == 8:
    if x.isupper():
        print("Sentence in uppercase")
    else:
        print("Sentence not in uppercase")