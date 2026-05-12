from Word import Word
from words import words
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
        new_sentence = []
        if self.sentence=="":
            return ""
        objects_to_process = self.objects

        question_prefixes = (
            "cómo es el",
            "cómo es la",
            "como es el",
            "como es la",
        )

        if self.sentence.startswith(question_prefixes):
            objects_to_process = self.objects[3:]

        for object in objects_to_process:
            new_word = object.get_new_word()
            if new_word != "":
                new_sentence.append(new_word)

        if len(new_sentence) == 0:
            return ""

        if new_sentence[-1] in ("de", "del"):
            for saved_word in words:
                if saved_word.get_name() == new_sentence[-1]:
                    new_word = saved_word.get_new_word()
                    if new_word != "":
                        new_sentence.append(new_word)
                    break

        return " ".join(new_sentence) + "."
