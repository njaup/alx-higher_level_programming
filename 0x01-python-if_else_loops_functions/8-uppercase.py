#!/usr/bin/python3

def uppercase(input_str):
    for m in input_str:
        if ord(m) >= a and ord(m) <= z:
            m = chr(ord(m) - 32)
            print("{}".format(m), end="")
