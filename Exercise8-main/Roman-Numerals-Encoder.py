
# Case:

# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses
# each Roman symbol in descending order: MDCLXVI.

# Example:
# solution(1000), should return 'M'

# Help:
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

# Remember that there can't be more than 3 identical symbols in a row.
# More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals

#  Solution:

def solution(n):
    result = ""
    length = len(str(n))
    x1 = n // 1000
    x0 = n % 1000
    x2 = x0 // 100
    x0 = x0 % 100
    x3 = x0 // 10
    x4 = x0 % 10
    while x1 > 0:
        result += "M"
        x1 -= 1
    if x2 >= 5:
        if x2 == 9:
            result += "CM"
        else:
            result += "D"
            x2 -= 5
            while x2 > 0:
                result += "C"
                x2 -= 1
    else:
        if x2 == 4:
            result += "CD"
        else:
            while x2 > 0:
                result += "C"
                x2 -= 1
    if x3 >= 5:
        if x3 == 9:
            result += "XC"
        else:
            result += "L"
            x3 -= 5
            while x3 > 0:
                result += "X"
                x3 -= 1
    else:
        if x3 == 4:
            result += "XL"
        else:
            while x3 > 0:
                result += "X"
                x3 -= 1
    if x4 >= 5:
        if x4 == 9:
            result += "IX"
        else:
            result += "V"
            x4 -= 5
            while x4 > 0:
                result += "I"
                x4 -= 1
    else:
        if x4 == 4:
            result += "IV"
        else:
            while x4 > 0:
                result += "I"
                x4 -= 1
    return result
  
