# import only system from os
import os
from time import sleep



# print out some text
print('hello geeks\n'*10)

# sleep for 2 seconds after printing output
sleep(1)


print(os.name)
# now call function we defined above
os.system('cls' if os.name == 'nt' else 'clear')


import sys
sys.stderr.write("\x1b[2J\x1b[H")

print("\033c")


print ('\n' * 100)