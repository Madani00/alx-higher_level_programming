#!/usr/bin/python3
for d in range(0, 100):
    if d == 99:
        print("{}".format(d))
    else:
        print("{:02}".format(d), end=", ")
