
# Case:

# Pirates have notorious difficulty with enunciating. They tend to blur all the letters together and scream at people.
# At long last, we need a way to unscramble what these pirates are saying.
# Write a function that will accept a jumble of letters as well as a dictionary, and output a list of words that the pirate might have meant.

# Example:
# grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
# Should return ["sport", "ports"].

# Return matches in the same order as in the dictionary. Return an empty array if there are no matches.

# Solution:

def grabscrab(word, possible_words):
    lst = []
    letters1 = {l:word.count(l) for l in word}
    for word in possible_words:
        letters2 = {l:word.count(l) for l in word}
        if letters1 == letters2:
            lst.append(word)
    return lst
