#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        for count in range(x):
            print("{}".format(my_list[count]), end='')
            elements_printed += 1
    except IndexError:
        pass
    print()
    return (elements_printed)
