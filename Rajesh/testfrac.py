
x = [1, 2, 3, 3, 1, 2, 3, 4, 5, 2, 4, 5]
y = [2, 2, 3, 6, 2, 4, 6, 8, 10, 2, 4, 5]
N = 12
Mx = 10
m = 0
match = 0

for i in range(N):
    for j in range(Mx):
        sx = x[i] * (j+1)
        sy = y[i] * (j+1)
        for k in range(i,N):
            print("xofk", x[k])
            print("yofk", y[k])
            print("sx :", sx)
            print("sy :", sy)
            if x[k] == sx:
                if y[k] == sy:
                    m = m + 1
    print("m: ", m)
    if m > match :
        match = m
        m = 0
        numa = x[i]
        numb = y[i]
    print("Element Num: ", i+1)

print("max num of fractions  : " , match)
print(" [x] = ",  numa )
print( "[Y] = ", numb)
