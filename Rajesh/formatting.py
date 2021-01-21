for i in range(1,13):
    print("No.  {0:2} squared is {1:3} and cubed is {2:4}" .format(i, i ** 2, i ** 3))

    print()

    myList = [1, 5, 5, 5, 5, 1]
max = myList[0]
indexOfMax = 0
for i in range(1, len(myList)):
    if myList[i] > max:
        max = myList[i]
        indexOfMax = i
print(indexOfMax)

x = True
y=False
z= False

if not x or y:
    print (1)
elif not x or not y and z:
    print (2)
elif not x or y or not y and x:
    print (3)
else:
    print (4)