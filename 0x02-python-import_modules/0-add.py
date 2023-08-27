#!/usr/bin/python3

a = 1
b = 2

imported_module = __import__('add_0')
add = imported_module.add

result = add(a, b)

print(f"{a} + {b} = {result}")

