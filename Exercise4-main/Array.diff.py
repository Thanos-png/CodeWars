
# Case:

# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order: array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other: array_diff([1,2,2,2,3],[2]) == [1,3]

# Solution:

def array_diff(a, b):
    c = a.copy()
    for item1 in c:
        f = False
        for item2 in b:
            if item1 == item2:
                f = True
                count = a.count(item1)
        if f:
            while count > 0:
                a.remove(item1)
                count -= 1
    return a
