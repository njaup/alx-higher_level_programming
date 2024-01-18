#!/usr/bin/python3

def print_last_digit(num):
    if num < 0:
        lastdig = num % -(10)
        print(-(lastdig), end='')
    else:
        lastdig = num % 10
        print(lastdig, end='')
    return abs(lastdig)
