
import random

def load_words(filename):
    words = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            words.append(line.strip())
    random.shuffle(words)
    return words

