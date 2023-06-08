#!/usr/bin/python3
def roman_to_int(roman_string):
    number = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0

    for symbol in roman_string:
        value = number.get(symbol, 0)
        if value == 0:
            return 0

        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value

    return result
