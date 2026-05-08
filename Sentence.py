from Word import Word
from words import words
from random import random
import re
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

    def get_word_object(self, word_name: str):
        for saved_word in words:
            if saved_word.get_name() == word_name:
                return saved_word
        return None

    def get_closing_punctuation(self, sentence: str):
        stripped_sentence = sentence.strip()

        if not stripped_sentence:
            return "."
        if stripped_sentence.startswith("¿") or stripped_sentence.endswith("?"):
            return "?"
        if stripped_sentence.startswith("¡") or stripped_sentence.endswith("!"):
            return "!"
        return "."

    def normalize_punctuation(self, sentence: str):
        normalized_sentence = re.sub(r"\s+", " ", sentence).strip()
        normalized_sentence = re.sub(r"\s+([,.;:!?])", r"\1", normalized_sentence)
        normalized_sentence = re.sub(r"([¿¡])\s+", r"\1", normalized_sentence)

        if not normalized_sentence:
            return ""

        closing_punctuation = self.get_closing_punctuation(normalized_sentence)
        if closing_punctuation == ".":
            closing_punctuation = self.get_closing_punctuation(self.sentence)
        normalized_sentence = normalized_sentence.rstrip(".,;:!?")

        if not normalized_sentence:
            return ""

        if closing_punctuation == "?" and not normalized_sentence.startswith("¿"):
            normalized_sentence = "¿" + normalized_sentence
        elif closing_punctuation == "!" and not normalized_sentence.startswith("¡"):
            normalized_sentence = "¡" + normalized_sentence

        return normalized_sentence + closing_punctuation

    def process_answer(self):
        sentence_parts = []

        if self.sentence == "":
            return ""

        for object in self.objects:
            if random() < 0.5:
                sentence_parts.append(object.get_name())

            next_word = object.get_new_word()
            if next_word:
                sentence_parts.append(next_word)

                next_word_object = self.get_word_object(next_word)
                if next_word_object is not None:
                    one_more_word = next_word_object.get_new_word()
                    if one_more_word:
                        sentence_parts.append(one_more_word)

        return self.normalize_punctuation(" ".join(sentence_parts))
