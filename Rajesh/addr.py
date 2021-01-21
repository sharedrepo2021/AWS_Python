import json

with open('address_db.json') as f:
    data = json.load(f)

print(json.dumps(data, indent=4))
for i in data:
    print(data[i])

