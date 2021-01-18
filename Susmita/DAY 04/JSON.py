import json

with open("Sample.json", "r") as read_file:
    address_dict = json.load(read_file)

print(json.dumps(address_dict, indent=4))

print(address_dict['glossary']['GlossDiv']['GlossList']['GlossEntry']
      ['GlossDef']['GlossSeeAlso'])

a = address_dict['glossary']['GlossDiv']['GlossList']['GlossEntry']['Abbrev']
print(a.split(':')[1])

