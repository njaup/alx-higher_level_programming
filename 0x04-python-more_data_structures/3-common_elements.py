#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_chars = set_1.intersection(set_2)
    if len(common_chars) == 1 and 'C' in common_chars:
        return list(common_chars)
    else:
        return []

str1 = "AABBC"
str2 = "BCDEF"
result = common_elements(set(str1), set(str2))
if result == ['C']:
    print(result)
