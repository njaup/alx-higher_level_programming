#!/usr/bin/python3

def uppercase(input_str):
    for m in input_str:
        if 'a' <= m <= 'z':
            uppercase_char = chr(ord(m) - ord('a') + ord('A'))
            print(uppercase_char, end='')
        else:
            print(m, end='')
