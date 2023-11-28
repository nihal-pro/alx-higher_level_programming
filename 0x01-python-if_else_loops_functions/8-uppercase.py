#!/usr/bin/python3
def uppercase(str):
    new_str = ''
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            new_str += chr(ord(ch) - 32)
        else:
            new_str += chr(ord(ch))
    print("{}".format(new_str))
