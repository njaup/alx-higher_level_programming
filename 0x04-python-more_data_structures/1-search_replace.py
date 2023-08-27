#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list

initial_list = [1, 2, 3, 2, 4, 2, 5]
new_list = search_replace(initial_list, 2, 0)
print(new_list)
