#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        i = '0' + str(i)
    print(i, end=", ")
print("{}".format(i + 1))
