#!/usr/bin/python3

def uppercase(input_str):
    for m in input_str:
        if ord(m) >= 97 and ord(m) <= 122:
            m = chr(ord(m) - 32)
            print("{}".format(m), end="")
