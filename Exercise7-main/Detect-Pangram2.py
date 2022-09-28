
# This is an alternative solution to the problem, but it is more time consuming.

# Solution:

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def is_pangram(s):
    result = True
    f = False
    i = 0
    for letter in alphabet:
        while i < len(s) and f == False:
            if letter == s[i]:
                f = True
        if f == False:
            result = False
    return result
