#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for elem in my_list:
            if count >= x:
                break
            print("{}".format(elem), end="")
            count += 1
        print("".format())
        return count
    except ValueError:
        print("ValueError")
