x = str(int(float('2')))
print(type(x))
print(x)

for i in 'abc':
    print(i.upper())

mylist = [['abc'], ['def', 'ghi']]
print(mylist[-1][-1][-1])


def eur_to_usd(euros, rate=0.8):
    return euros * rate
print(eur_to_usd(10))

def foo(a = 1, b = 2):
    return a + b
price = foo(b = 4)
print(price)

d = {
    "food": {
        "rice":
            {
                "weight": 30.1,
                "taste": "good",
                "forms": ["boiled"]
            },
        "banana":
            {
                "weight": 19,
                "taste": "excellent",
            }
    }
}

print(d['food']['banana']['taste'])


def foo(x):
    return x * 2

print(foo("Hello"))

