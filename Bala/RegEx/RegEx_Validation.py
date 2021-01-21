import re

# Validation

name_pattern = re.compile('(^[A-Z])([a-zA-Z]*$)')
phone_pattern = re.compile('\(\w{3}\)[-.]\w{3}[-.]\w{4}')
email_pattern = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')


phone = '0'

# while True:
#     fname = input('Enter the Name: ')
#
#     if re.findall(name_pattern, fname):
#         print("First Name: {}".format(fname.capitalize()))
#         break
#     else:
#         print("false")


# while True:
#     phone = input('Enter Phone Number: ')
#     if re.findall(phone_pattern, phone):
#         print("Phone No: {}".format(phone))
#         break
#     else:
#         print("false")

while True:
    email = input('Enter Email Address: ')
    if re.findall(email_pattern, email):
        print('Email Address: ', email)
        break
    else:
        print('false')