#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0

    roman_nume = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    dec = [roman_num[x] for x in roman_string]
    output = 0
    for i in range(len(dec)):
        output += dec[i]
        if dec[i - 1] < dec[i] and i != 0:
            output -= (dec[i - 1] + dec[i - 1])
    return output
