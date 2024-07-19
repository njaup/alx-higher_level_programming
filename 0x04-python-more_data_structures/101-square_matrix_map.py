#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda col: col**2, row)), matrix))
======================================================================

vi 102-complex_delete.py
……………………………………………………………………………………………………………
#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for k, v in tmp.items():
        if value == v:
            my_dict.pop(k)
    return my_dict
