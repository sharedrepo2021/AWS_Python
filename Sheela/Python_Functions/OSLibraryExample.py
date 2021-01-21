import os

#Name of the operating system

print(os.name)

#returns the Current Working Directory(CWD)

print(os.getcwd())

#A file old.txt can be renamed to new.txt
file = "Sample.txt"
os.rename(file, 'Sample1.txt')


#Python OS Error

try:
    # If the file does not exist,
    # then it would throw an IOError
    filename = 'Sample14444.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()

except IOError as e:

    # print(os.error) will <class 'OSError'>
    print('Problem reading: ' + filename)
    print(e)