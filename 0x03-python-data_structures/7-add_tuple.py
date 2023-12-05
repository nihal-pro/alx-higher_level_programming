#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) > 0:
        a_integer1 = tuple_a[0]
    else:
        a_integer1 = 0

    if len(tuple_a) > 1:
        a_integer2 = tuple_a[1]
    else:
        a_integer2 = 0

    if len(tuple_b) > 0:
        b_integer1 = tuple_b[0]
    else:
        b_integer1 = 0

    if len(tuple_b) > 1:
        b_integer2 = tuple_b[1]
    else:
        b_integer2 = 0

    return (a_integer1 + b_integer1, a_integer2 + b_integer2)
