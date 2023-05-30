#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if j < 123 and j > 96:
            j = j - 32
        print("{}".format(chr(j)), end="")
    print("")
