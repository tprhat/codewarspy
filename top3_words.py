import re
from collections import Counter


def top_3_words(text):
    words = re.sub(r" '+ ", ' ', text.lower())
    words = re.findall(r"[a-z']+", words)

    word_counter = {}
    for w in words:
        if w not in word_counter:
            word_counter[w] = 1
        else:
            word_counter[w] += 1
    word_counter = dict(sorted(word_counter.items(), key=lambda item: item[1], reverse=True))
    top3 = []
    for k in word_counter:
        top3.append(k)
        if len(top3) == 3:
            break
    return top3


# using collections -- TO DO: LEARN THIS MODULE
def top_3_words_simple(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w, _ in c.most_common(3)]
