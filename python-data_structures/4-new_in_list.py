#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_aux = []
    for i in range(len(my_list)):
        if idx >= 0 and idx < len(my_list) and i == idx:
            my_list_aux.append(element)
        else:
            my_list_aux.append(my_list[i])
    return my_list_aux
