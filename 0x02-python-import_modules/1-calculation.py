#!/usr/bin/python3

from calculator_1 import addition, subtraction, multiplication, division

a = 10
b = 5

result_add = addition(a, b)
result_subtract = subtraction(a, b)
result_multiply = multiplication(a, b)
result_divide = division(a, b)

print("Results:")
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
