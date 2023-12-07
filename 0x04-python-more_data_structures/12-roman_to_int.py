#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    array = []
    if roman_string is not None and isinstance(roman_string, str):
        roman = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        for ch in roman_string:
            if ch in roman:
                array.append(roman[ch])
                # print(array)
        for i in range(len(array) - 1):
            if array[i] >= array[i + 1]:
                number += array[i]
                # print(" -> + "number)
            elif array[i] < array[i + 1]:
                number -= array[i]
                # print(" -> -"number)
        number += array[len(array) - 1]
        # print(" -> last number :", number)
    return number
