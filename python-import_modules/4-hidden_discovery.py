#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    arr = []
    for i in range(len(dir(hidden_4))):
        if dir(hidden_4)[i][0] != '_' and dir(hidden_4)[i][1] != '_':
            arr.append(dir(hidden_4)[i])
    arr.sort()
    for i in range(len(arr)):
        print(arr[i])
