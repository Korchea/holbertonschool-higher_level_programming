#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 1:
        print("0")
    elif length == 2:
        print("{}".format(int(argv[1])))
    else:
        sum = 0
        for i in range(1, length):
            sum += int(argv[i])
        print("{}".format(sum))
