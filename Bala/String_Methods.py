str00 = '01234567890123456789012345678901234567890'
str01 = '   01023 3333 6789 90923 152 123         '
str02 = 'jenny james JENNY JAMES'
str03 = '123.9'
str04 = 'Demo001'

print('Fill         : ', str01.zfill(56))

print('find         : ', str01.find('12'))
print('Index        : ', str01.index('12'))
print('replace      : ', str01.replace('33', '99'))

print('Partition    : ', str01.partition(' '))
print('Split        : ', str01.split(' '))

print('Left Strip   : ', str01.lstrip())
print('Right Strip  : ', str01.rstrip())
print('Full Strip   : ', str01.strip())

print('Upper        : ', str02.upper())
print('Lower        : ', str02.lower())
print('Title        : ', str02.title())
print('Swap         : ', str02.swapcase())
print('Capitalize   : ', str02.capitalize())
print('Case fold    : ', str02.casefold())

print('Digit        : ', str03.isdigit())
print('Numeric      : ', str03.isnumeric())

if str03.isnumeric():
    num01 = float(str03)
else:
    num01 = str(str03)
print('Number       : ', type(num01))

print('alphanumeric : ', str04.isalnum())
print('identifier   : ', str04.isidentifier())

print('Count of 3   : ', str01.count('3'))
