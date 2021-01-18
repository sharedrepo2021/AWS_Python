import json

with open(r"Test1.json", "r") as f:
    #print(f.read())
    data = json.load(f)
    print(json.dumps(data, indent=4))


print(data["AddressBook"]["Biji"]["Phone"][2])
