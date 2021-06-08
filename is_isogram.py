# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore
# letter case.

def is_isogram(string):
    used_letters = []
    for i in string.lower():
        if i in used_letters:
            return False
        used_letters.append(i)
    return True


def is_isogram_bestsolution(string):
    return len(string) == len(set(string.lower()))
