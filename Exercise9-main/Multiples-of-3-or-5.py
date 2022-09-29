
# Case:

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return
# 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.

# Solution:

def solution(number):
    sum = 0
    if number > 3:
        num = str(number)
        num = int(num[-1])
        if num > 5:
            a = num - 5
            j = 0
            for i in range(number,0,-5):
                if i > 0:
                    sum += i
                    j += 1
            sum -= a * j
        elif num < 5 and num != 0:
            j = 0
            for i in range(number,0,-5):
                if i > 0:
                    sum += i
                    j += 1
            sum -= num * j
        else:
            for i in range(number-5,0,-5):
                if i > 0:
                    sum += i
        for i in range(3,number,3):
            if i % 5 != 0:
                sum += i
    return sum
