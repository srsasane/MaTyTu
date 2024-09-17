

import random
import time

class TypingTutor:
    def __init__(self, filename):
        self.filename = filename
        self.words = []
        self.word_id = None
        self.word = None
        self.start_time = None
        self.load_words()

    def load_words(self):
        with open(self.filename, 'r', encoding="utf-8") as f:
            self.words = [line.strip() for line in f]
        random.shuffle(self.words)

    def get_word(self):
        self.word_id = random.randint(0, len(self.words) - 1)
        self.word = self.words[self.word_id]
        self.start_time = time.time()
        print('From L24 TypingTutor.py :'+self.word)
        return self.word
    

    # self.words = []
    #   f = open(self.filename, 'r', encoding="utf-8")
    #    for line in f:
    #        self.words.append(line.strip())
    #        random.shuffle(self.words)

    def check_answer(self, answer):
        if answer == self.word:
            end_time = time.time()
            time_taken = float(end_time - self.start_time)
            return True, time_taken
        return False, None
