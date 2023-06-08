#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    np = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]))
            np += 1
        except Exception:
            print()
            return np
    print()
    return np
