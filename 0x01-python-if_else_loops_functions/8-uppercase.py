#!/usr/bin/python3

def uppercase(input_str):
    result = ""
    for char in input_str:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        result += char

    print(result)
    print(f"({len(result)} chars long)")
