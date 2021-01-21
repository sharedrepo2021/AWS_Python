import json as js
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(js.dumps(thisdict["colors"][1], indent=4))

thisdict.update({"year": 2020})

print(js.dumps(thisdict, indent=4))

thisdict["trim"] = "SUV"

print(js.dumps(thisdict, indent=4))
thisdict.update({"Option": "Full"})

print(js.dumps(thisdict, indent=4))

print(thisdict.items())

for x, y in thisdict.items():
    print(x, y)