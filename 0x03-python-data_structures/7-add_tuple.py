#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tupa = (tuple_a[0], 0)
    elif len(tuple_a) == 0:
        tupa = (0, 0)
    else:
        tupa = tuple_a
    if len(tuple_b) == 1:
        tupb = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        tupb = (0, 0)
    else:
        tupb = tuple_b

    int1 = tupa[0] + tupb[0]
    int2 = tupa[1] + tupb[1]
    new_tuple = (int1, int2)
    return new_tuple
