#!/usr/bin/python3
def magic_string(static={"i": 0}):
    static["i"] += 1
    return str("BestSchool, " * static["i"])[:-2]
