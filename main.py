from Sentence import Sentence
import unicodedata
from Version import Version
from Debug import Debug
Debug(f"Welcome to GuadalIA M{Version.model}.{Version.build} !")
import aitrainer_script
def main():
    while True:
        sentence_input = input("Enter a sentence: ")
        sentence_input = sentence_input.lower()
        sentence_input = unicodedata.normalize("NFD", sentence_input)
        sentence_input = "".join(
            c for c in sentence_input
            if unicodedata.category(c) != "Mn"
        )
        sentence = Sentence(sentence_input)
        sentence.add_objects()
        processed_sentence = sentence.process_answer()
        print("Answer:", processed_sentence)
if __name__ == "__main__":
    main()
