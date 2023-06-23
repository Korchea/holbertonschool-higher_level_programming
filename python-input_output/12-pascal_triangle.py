#!/usr/bin/python3
def pascal_triangle(n):
    pascal = []
    for i in range(n):
        pascal.append([1])
        for j in range(i):
            if j == i - 1:
                pascal[i].append(1)
            else:
                pascal[i].append(pascal[i-1][j+1] + pascal[i-1][j])
    return pascal
