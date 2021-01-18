with open(r"E:\Study\Python\Data\Input.txt") as f:
    print(f.read())

with open(r"E:\Study\Python\Data\Output.txt", 'a') as f:
    print(f.write("abc"))