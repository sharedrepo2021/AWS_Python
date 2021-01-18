

def abc(**kargs):
    if 'Name' in kargs and 'Phone' in kargs:
        print('Hello {}, your phone number is {}'.format(kargs['Name'], kargs['Phone']))
    else:
        print('Hello Mr. I dont know anything about you')


abc(Name='Dipan', Phone='2342345345')


import json

json.dump()
