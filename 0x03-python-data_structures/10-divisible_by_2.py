#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    aux = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            aux.append(True)
        else:
            aux.append(False)
    return aux