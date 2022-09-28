
# Case:

# Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).

# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

# Solution:

def solution(string, ending):
    f = False
    size = len(ending)
    if size == 0:
        f = True
    elif string[-size:] == ending:
        f = True
    return f
