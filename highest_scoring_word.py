# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

def helper(x):
    return ord(x) - ord('a') + 1


def high(x):
    words = x.split(' ')
    max_score = 0
    max_word = ''
    for w in words:
        s = sum(map(helper, w))
        if s > max_score:
            max_word = w
            max_score = s
    return max_word


print(high('man i need a taxi up to ubud'))  # = 'taxi'
print(high('what time are we climbing up the volcano'))  # = 'volcano'
