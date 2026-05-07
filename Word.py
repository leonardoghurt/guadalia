from random import randint, choice
import words
class Word:
    def __init__(self, word: str):
        self.word = word
        self.nextwords = ["what"]
        words.words.append(self)
    def add_next_word(self, word: str):
        self.nextwords.append(word)
    def get_name(self):
        return self.word
    def get_new_word(self):
        return choice(self.nextwords)