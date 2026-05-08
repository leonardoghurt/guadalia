from random import choice
import words
class Word:
    def __init__(self, word: str):
        self.word = word
        self.nextwords = []
        words.words.append(self)
    def add_next_word(self, word: str):
        if word:
            self.nextwords.append(word)
    def get_name(self):
        return self.word
    def get_new_word(self):
        if not self.nextwords:
            return ""
        return choice(self.nextwords)
