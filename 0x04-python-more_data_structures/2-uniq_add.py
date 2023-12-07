#!/usr/bin/python3
def uniq_add(my_list=[]):
    Result = 0
    new = set(my_list)
    for num in new:
        Result += num
        # to new if num duplicate or not and result -> print(num, Result)
    return Result
