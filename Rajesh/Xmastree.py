x = 5
y = 1

while y < 6:
    for i in range(x):
        z = i + y
        print(("* " * z).center(50))
    x = x + 2
    y = y + 2
    z = i - y

for j in range(x - y):
    print("****".center(49))