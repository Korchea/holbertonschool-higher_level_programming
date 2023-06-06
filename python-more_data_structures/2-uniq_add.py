#!/usr/bin/python3
def uniq_add(my_list=[]):
    to_sum = []
    for i in range(len(my_list)):
        rep = False
        for j in range(len(to_sum)):
            if my_list[i] == to_sum[j]:
                rep = True
                break
        if not rep:
            to_sum.append(my_list[i])
    sum = 0
    for j in range(len(to_sum)):
        sum += to_sum[j]
    return sum
