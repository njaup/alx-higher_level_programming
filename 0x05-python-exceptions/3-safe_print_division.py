#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        value = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    finally:
        print("Inside result: {}".format(value) if 'result' in locals() else "Inside result: None")
        return value
