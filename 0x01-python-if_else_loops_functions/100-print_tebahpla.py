#!/usr/bin/python3

current = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - current)), end="")
    current = 32 if current == 0 else 0
