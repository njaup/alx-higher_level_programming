def divisible_by_2(my_list=[]):
    total = []
    for count in my_list:
        total.append(count % 2 == 0)
    return total
