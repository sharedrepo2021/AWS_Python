from datetime import datetime

now = datetime.now()

print(now)
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

if current_time <= '22:28:59':
    print('yes')
else:
    print('no')