import time

print(time.asctime())

current_time = time.time()
print(current_time)

i = 5
while i < 10:
    print("print somthing", i)
    i = i + 1

print(current_time)
print(current_time-time.time())

for x in range(0,6):
    print(x)

print(current_time)
print(current_time-time.time())

