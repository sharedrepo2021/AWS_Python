data0 = "01234567890123456789012345678901234567890123456789"
data1 = "hello, my first code in my python written in my pycharm ."
data2 = "Python Is A Language \n easy to learn."
data3 = "   SHEELA_01   "
data4 = "My name is Ståle"
data5 = "Ex\tpan\tdab\tle"
data6 = "My name is {0}, I'm {1}"
data7 = "2021"
data8 = {'x':'John', 'y':'Wick'}
data9 = ("python", "string", "methods")
data10 = "John"
data11 = "Wick"
data12 = "my"
data13 = "I am John and today is my first day"

a = data1.capitalize()
b = data2.casefold()
c = data3.center(20)
d = data1.count("in", 25, 50)
e = data4.encode()
f = data1.endswith("", 10, 20)
g = data5.expandtabs(10)
h = data1.find("ni")
i = data1.index("in")
j = data6.format("sheela", 38)
k = data7.join(data9)
l = data3.ljust(20, "*")
m = data1.upper()
n = data3.strip()
o = data2.partition("A")
p = data1.replace("my", "our", 2)
q = data2.split()
r = data2.split(" ", 2)
s = data2.splitlines(False)
t = data1.startswith("h", 0, 50)
u = data2.swapcase()
v = data3.lower()
w = data7.zfill(10)
mytable = data13.maketrans(data10, data11, data12)
translatedata = data13.translate(mytable)

print(type(data0))
print("capitalize method ::::: " , a)
print("casefold method ::::: ", b)
print("center method ::::: ", c)
print("count method ::::: ", d)
print("encode method ::::: ", e)
print(data4.encode(encoding="ascii", errors="replace"))
print("endswith method T or F ::::: ", f)
print("expand tabs method ::::: ", g)
print("find  a string:::::", h)
print("index  a string :::::",  i)
print("format method:::::", j)
print("{x}'s last name is {y}".format_map(data8))
print("Join method to join the string ::::", k)
print("Ljust method ::::::", l)
print("upper method ::::::", m)
print("strip method trims both ends::::::", n)
print("partition method splits only in 3 ::::::", o)
print("replace method :::::::", p)
print("split method splits all the words not only in 3 parts :::::::", q)
print("split method with passing variables and max split :::::::", r)
print("split lines method splits with breakline :::::::", s)
print("startswith method T or F ::::: ", t)
print("swapcase method  ::::: ", u)
print("lower method  ::::: ", v)
print("zfill method to fill zero in the start  ::::: ", w)
print("maketrans and translate , replace and remove strings  ::::: ", translatedata)
print("is data 3  alpha numberic::::",  data3.isalnum())
print("is data 3  identifier::::",  data3.isidentifier())
print("is data 3  alpha::::",  data3.isalpha())
print("is data 7 digit::::", data7.isdigit())
print("is data 7 numeric::::", data7.isnumeric())
print("is data 2 printable::::", data2.isprintable())
print("is data 1 is lower::::", data1.islower())
print("is data 2 is title::::", data2.istitle())
print("is data 3 is upper::::", data3.isupper())
