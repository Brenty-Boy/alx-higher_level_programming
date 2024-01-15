#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    numb = [roman_dict[x] for x in roman_string]
    output = 0
    for i in range(len(numb)):
        output += numb[i]
        if numb[i - 1] < numb[i] and i != 0:
            output -= (numb[i - 1] + numb[i - 1])
    return output
