import json
n = int(input("Enter one number: "))

def frec(n):
    if n == 1:
        return 1
    else:
        return  n * frec(n - 1)


if __name__ == '__main__':
    print(frec(n))