
# This is an easier way to do it, but i thought it would be boring.

# Solution:

def solution(number):
    sum = 0
    if number > 3:
        for i in range(5,number,5):
            sum += i
        for i in range(3,number,3):
            if i % 5 != 0:
                sum += i
    return sum
  
