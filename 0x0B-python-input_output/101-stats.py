#!/usr/bin/python3

""""
a function that reads stdin line by line and computes metrics
"""

import sys

FileSize = 0
status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
number_line = 0
try:
    for line in sys.stdin:
        seperater = line.split()
        if len(seperater) >= 2:
            sure = number_line
            if seperater[-2] in status_code:
                status_code[seperater[-2]] += 1
                number_line += 1
            try:
                FileSize += int(seperater[-1])
                if sure == number_line:
                    number_line += 1
            except Exception:
                if sure == number_line:
                    continue
        if number_line % 10 == 0:
            print("File size: {:d}".format(FileSize))
            for key, val in sorted(status_code.items()):
                if val:
                    print("{:s}: {:d}".format(key, val))
    print("File size: {:d}".format(FileSize))
    for key, val in sorted(status_code.items()):
        if val:
            print("{:s}: {:d}".format(key, val))
except KeyboardInterrupt:
    print("File size: {:d}".format(FileSize))
    for key, val in sorted(status_code.items()):
        if val:
            print("{:s}: {:d}".format(key, val))
