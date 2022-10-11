
# Case:

# Digital Cypher assigns to each letter of the alphabet unique number. For example:
#  a  b  c  d  e  f  g  h  i  j  k  l  m
#  1  2  3  4  5  6  7  8  9 10 11 12 13
#  n  o  p  q  r  s  t  u  v  w  x  y  z
# 14 15 16 17 18 19 20 21 22 23 24 25 26

# Instead of letters in encrypted word we write the corresponding number, eg. The word scout:
# s  c  o  u  t
# 19  3 15 21 20

# Then we add to each obtained digit consecutive digits from the key. For example. In case of key equal to 1939 :
#   s  c  o  u  t
#  19  3 15 21 20
# + 1  9  3  9  1
# ---------------
#  20 12 18 30 21

# Task: Write a function that accepts str string and key number and returns an array of integers representing encoded str.
# Input / Output: 
# The str input string consists of lowercase characters only.
# The key input number is a positive integer.

# Example:
# Encode("scout",1939);  ==>  [ 20, 12, 18, 30, 21]
# Encode("masterpiece",1939);  ==>  [ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]

# Solution:

def encode(message, key):
    result = []
    for i in range(len(message)):
        result.append(ord(message[i]) - 96 + int(str(key)[i % len(str(key))]))
    return result

# The answer to the solution looks small, but in reality it is just compressed.
