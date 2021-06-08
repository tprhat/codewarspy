# Your task is to sort a given string. Each word in the string will contain a single number. This number is the
# position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input String will only contain valid
# consecutive numbers.

def order(sentence):
    new_list = sentence.split(' ')
    words = {}
    for x in new_list:
        for y in x:
            if y.isdigit():
                words[y] = x
                break
    words = dict(sorted(words.items()))
    return ' '.join(words.values())


print(order("4of Fo1r pe6ople g3ood th5e the2"))
