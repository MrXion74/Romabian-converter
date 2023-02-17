def arabic_to_roman(num):
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    symbols = [
        'M', 'CM', 'D', 'CD',
        'C', 'XC', 'L', 'XL',
        'X', 'IX', 'V', 'IV',
        'I'
    ]
    result = ''
    i = 0
    while num > 0:
        if num - values[i] >= 0:
            result += symbols[i]
            num -= values[i]
        else:
            i += 1
    return result

def roman_to_arabic(roman):
    values = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
    }
    result = 0
    for i in range(len(roman)):
        if i > 0 and values[roman[i]] > values[roman[i-1]]:
            result += values[roman[i]] - 2*values[roman[i-1]]
        else:
            result += values[roman[i]]
    return result
