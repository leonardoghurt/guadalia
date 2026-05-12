from Token import Token
from tokens import tokens
class Sentence:
    def __init__(self, sentence: str):
        self.sentence = sentence
        self.objects = []
    def add_objects(self):
        self.objects = []
        split_words = self.sentence.split()
        
        for word in split_words:
            existing_word = None

            for saved_word in tokens:
                if saved_word.get_name() == word:
                    existing_word = saved_word
                    break

            if existing_word is None:
                existing_word = Token(word)

            self.objects.append(existing_word)

    def add_next(self):
        for i, current_word in enumerate(self.objects[:-1]):
            next_word = self.objects[i + 1].get_name()
            current_word.add_next_token(next_word)
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
            "cómo es",
            "como es",
            "qué es",
            "que es",
        )
        for question_prefix in question_prefixes:
            if self.sentence.startswith(question_prefix):
                objects_to_process = self.objects[len(question_prefix.split()):]
                break
        for object in objects_to_process:
            new_word = object.get_new_token()
            if new_word != "":
                new_sentence.append(new_word)
        if len(new_sentence) == 0:
            return ""
        return (" ".join(new_sentence) + ".").capitalize()