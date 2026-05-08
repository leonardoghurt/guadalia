from Word import Word
from words import words
from random import random
class Sentence:
    def __init__(self, sentence: str):
        self.sentence = sentence
        self.objects = []
    def add_objects(self):
        self.objects = []
        split_words = self.sentence.split()

        for word in split_words:
            existing_word = None

            for saved_word in words:
                if saved_word.get_name() == word:
                    existing_word = saved_word
                    break

            if existing_word is None:
                existing_word = Word(word)

            self.objects.append(existing_word)

    def add_next(self):
        for i, current_word in enumerate(self.objects[:-1]):
            next_word = self.objects[i + 1].get_name()
            current_word.add_next_word(next_word)
    def process_answer(self):
        new_sentence = ""
        if self.sentence=="":
            return ""
        for object in self.objects:
            if random() < 0.5:
                new_sentence+=object.get_name()+" "
            new_sentence+=object.get_new_word()+" "
            try:
                onemoreword = Word(new_sentence.split()[-1])
                new_sentence+=onemoreword.get_new_word()+" "
            except: pass
        new_sentence = new_sentence.removesuffix(".")
        new_sentence+="."
        return new_sentence
