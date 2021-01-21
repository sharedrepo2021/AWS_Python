import os

x = "Hello"
b = "hi"


try:
  print(x)

except:
  print("An exception occurred")


try:
  print(b)
except NameError:
  print("Variable b is not defined")
except:
  print("Something else went wrong")


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# x = -1
#
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")




'''
if not type(x) is int:
  raise TypeError("Only integers are allowed")
'''
