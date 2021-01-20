
def abc(**kargs):

    if 'Name' in kargs and 'phone' in kargs:
        print('hello {},your phone number is {}'.format(kargs['Name'], kargs['phone']))
    else:
        print("i don't know anything about you ")

abc(Name='BIJI', phone='334')
