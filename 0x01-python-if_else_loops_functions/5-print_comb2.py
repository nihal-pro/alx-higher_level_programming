#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        separated = "\n"
    else:
        separated = ", "
    print("{:02d}".format(num), end=separated)
