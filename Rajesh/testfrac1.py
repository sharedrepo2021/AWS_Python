
x = [10000000000000, 1, 2, 3, 3, 1, 2, 3, 4000, 3, 2, 4, 5]
y = [25666222222222, 1, 2, 3, 6, 2, 4, 6, 800000, 10, 2, 4, 5]
z = []
N = 13
m = 1
match = 0

for i in range(N):
    z.append(x[i] / y[i])

z.sort()
print(z)

k = 1
i = 0

while k!= N:
    if z[i] == z[k]:
       m = m + 1
       k = k + 1
    elif z[k] > z[i]:
        if match < m :
            match = m
        m = 1
        i = k
        k = k + 1
if m > match :
    match = m
print("Max factor : ", match)


