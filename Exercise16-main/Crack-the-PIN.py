
# Case:

# Given is a md5 hash of a five digits long PIN. It is given as string. Md5 is a function to hash your password: "password123" ===>
# "482c811da5d5b4bc6d497ffa98491e38"
# Why is this useful? Hash functions like md5 can create a hash from string in a short time and it is impossible to find out the password, if you only got
# the hash. The only way is cracking it, means try every combination, hash it and compare it with the hash you want to crack. (There are also other
# ways of attacking md5 but that's another story) Every Website and OS is storing their passwords as hashes, so if a hacker gets access to the
# database, he can do nothing, as long the password is safe enough.
# Note: Many languages have build in tools to hash md5. If not, you can write your own md5 function or google for an example.
# Your task is to return the cracked PIN as string.

# Solution:

import hashlib

def crack(hash):
    for i in range(100000):
        password = f"{i:05d}"
        if hashlib.md5(password.encode()).hexdigest() == hash:
            return password
