
# Case:

# Here are the conditions:
# 1. Your message is a string containing space separated words.
# 2. You need to encrypt each word in the message using the following rules:
#    - The first letter must be converted to its ASCII code.
#    - The second letter must be switched with the last letter
# 3. Keepin' it simple: There are no special characters in the input.

# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

# Solution:

def encrypt_this(text):
    words = text.split(" ")
    result = ""
    if text != "":
        for word in words:
            result += str(ord(word[0]))
            if len(word) > 1:
                result += word[-1]
                for i in range(2, len(word)-1):
                    result += word[i]
                if len(word) > 2:
                    result += word[1]
            result += " "
    return result[:-1]
