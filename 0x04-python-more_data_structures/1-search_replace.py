#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list

if __name__ == "__main__":
    initial_list = [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
    new_list = search_replace(initial_list, 89, 2)
    print(new_list)
