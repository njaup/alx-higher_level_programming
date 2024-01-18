#!/usr/bin/python3

def print_last_digit(number):
    if not isinstance(number, int) or number < 0:
        print("Please provide a non-negative integer.")
        return None
    last_digit = number % 10
    print("Last digit:", last_digit)
    return last_digit
