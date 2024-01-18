#!/usr/bin/python3

def uppercase(input_str):
    result = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
        result += char

    print(result)
    print(f"({len(result)} chars long)")
