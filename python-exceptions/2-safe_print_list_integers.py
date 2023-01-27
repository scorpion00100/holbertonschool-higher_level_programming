#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    value = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            value += 1
        except (TypeError, ValueError):
            continue
    print("")
    return value
