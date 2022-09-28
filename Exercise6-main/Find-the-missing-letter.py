
# Case:

# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Examples:
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

# Solution:

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

def find_missing_letter(chars):
    chars_lower = []
    f = True
    i = -1
    for char in chars:
        chars_lower.append(char.lower())
    if chars != chars_lower:
        f = False
    while i < 25:
        i += 1
        if alphabet[i] == chars_lower[0]:
            k = i + 1
            j = 1
            while alphabet[k] == chars_lower[j]:
                k += 1
                j += 1
            if f == True:
                return alphabet[k]
            else:
                return alphabet[k].upper()
