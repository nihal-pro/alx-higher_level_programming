#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) > 0:
        max = my_list[0]
        for idx in range(len(my_list)):
            if my_list[idx] > max:
                max = my_list[idx]
                idx += 1
        return (max)
    else:
        return (None)
