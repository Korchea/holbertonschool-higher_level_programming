#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    np = 0
    oor = True
    for i in range(x):
        try:
            print(my_list[i], end="")
            np += 1
        except:
            print()
            return np
    print()
    return np
