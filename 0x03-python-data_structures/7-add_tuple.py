#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    padded_tuple_a = tuple_a + (0, 0)[:max(0, 2 - len(tuple_a))]
    padded_tuple_b = tuple_b + (0, 0)[:max(0, 2 - len(tuple_b))]
    result_1 = padded_tuple_a[0] + padded_tuple_b[0]
    result_2 = padded_tuple_a[1] + padded_tuple_b[1]
    result_tuple = (result_1, result_2)
    return result_tuple
