a = "i have"
b = 5
c = "apples"
d = str(b)

print(a + " " + d + " " + c)
print(c.upper())
print(c.lower())
# e=capitalize
# capi
print(c.capitalize())
print(c.casefold())
print(c.center(20))
print(c.encode())
fruits = ["fdf", "Fdd", "Dffd"]
print("#".join(fruits))
print(fruits.count("Dffd"))
print(c.endswith("s"))

print(c.expandtabs(2000))
print(c.format())
print(c.find("s"))
print(c.index("l"))
print(c.format_map(3))
print(c.isalnum())
print(c.isalpha())
print(c.isdecimal())
print(c.isdigit())
print(c.isidentifier())
print(c.islower())
print(c.isnumeric())
print(c.isprintable())
print(c.isspace())
print(c.istitle())
#print(c.issupper())

print(c.join("#"))
print(c.ljust(20))
print(c.lstrip())


h = c.maketrans("e","k")
print(c.translate(h))
print(c.title())
print(c.zfill(100))
print(c.swapcase())
print(c.strip("a"))
print(c.partition("l"))