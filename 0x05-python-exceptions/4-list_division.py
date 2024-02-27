#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for count in range(list_length):
            try:
                number1 = my_list_1[count] if count < len(my_list_1) else None
                number2 = my_list_2[count] if count < len(my_list_2) else None

                if number1 is None or number2 is None:
                    raise IndexError("out of range")

                if isinstance(number1, (int, float)) and isinstance(number2, (int, float)):
                    if number2 == 0:
                        raise ZeroDivisionError("division by 0")
                    result.append(number1 / number2)
                else:
                    raise TypeError("wrong type")
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
    finally:
        return result
