'''
        This program deals with String Slicing
        M  i  r  i  t  h  i  k  a  -  B  a  l  a  m  u  r  u  g  a  n
        0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7  8  9  0
      -21-20-19-18-17-16-15-14-13-12-11-10-09-08-07-06-05-04-03-02-01
'''


full_name = "Mirithika-Balamurugan"
len_name = len(full_name)
incre = len_name - 1

print('Full Name:    ', full_name)
print('Length   :    ', len_name)

print('the reversed name\n')
while incre < len_name:
    print(full_name[incre], end='')
    incre = incre - 1
    if incre == -1:
        incre = len_name + 5
