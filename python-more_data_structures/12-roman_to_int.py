#!/usr/bin/python3
def roman_to_int(roman_string):
    number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    flag = False
    if not roman_string:
        return 0
    if len(roman_string) == 1:
        sum = number[roman_string[0]]
    for i in range(1, len(roman_string)):
        for key, value in number.items():
            if roman_string[i] == key:
                for pre_key, pre_value in number.items():
                    if roman_string[i - 1] == pre_key and pre_value >= value:
                        if i == 1:
                            sum += value + pre_value
                        else:
                            sum += value
                        flag = True
                        break
                    elif roman_string[i - 1] == pre_key and pre_value < value:
                        if flag:
                            sum += (value - 2*pre_value)
                        else:
                            sum += (value - pre_value)
                        flag = False
                        break
                    elif pre_key == 'M':
                        return 0
                break
            elif key == 'M':
                return 0
    return sum
