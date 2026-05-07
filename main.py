from Sentence import Sentence
import aitrainer_script
def main():
    while True:
        sentence_input = input("Enter a sentence: ")
        sentence = Sentence(sentence_input)
        sentence.add_objects_add_next()
        processed_sentence = sentence.process_answer()
        print("Answer:", processed_sentence)
if __name__ == "__main__":
    main()