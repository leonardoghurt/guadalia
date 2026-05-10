from Debug import Debug
import unicodedata
from pathlib import Path
from Sentence import Sentence


def normalize_sentence(sentence: str) -> str:
    sentence = sentence.lower()
    sentence = unicodedata.normalize("NFD", sentence)
    return "".join(
        character for character in sentence
        if unicodedata.category(character) != "Mn"
    )


def get_sentence_file_number(path: Path) -> int:
    try:
        return int(path.stem.removeprefix("sn"))
    except ValueError:
        return 0


def train_sentence(line: str) -> bool:
    normalized_line = normalize_sentence(line.strip())

    if normalized_line == "":
        return False

    sentence = Sentence(normalized_line)
    sentence.add_objects()
    sentence.add_next()
    return True


def train_file(path: Path) -> int:
    trained_sentences = 0

    with path.open("r", encoding="utf-8") as sentence_file:
        for line in sentence_file:
            if train_sentence(line):
                trained_sentences += 1

    return trained_sentences


def train_all_sentence_files() -> int:
    sentence_files = sorted(
        Path(".").glob("*.txt"),
        key=get_sentence_file_number,
    )
    trained_sentences = 0

    for sentence_file in sentence_files:
        trained_sentences += train_file(sentence_file)

    Debug(
        f"Trained {trained_sentences} sentences "
        f"from {len(sentence_files)} sentence files"
    )
    return trained_sentences


train_all_sentence_files()
