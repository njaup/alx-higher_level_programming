#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for index in range(x):
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end="")
                i += 1
    except IndexError:
        pass
    print()
    return (i)
