#!/usr/bin/python3
for num in range(1, 100):
    separated = ", "
    if num == 89:
        separated = "\n"
    if num / 10 < num % 10:
        print("{:02d}".format(num), end=separated)
