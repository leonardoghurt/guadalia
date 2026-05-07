from pathlib import Path

from Sentence import Sentence


def create_sentences_from_txt_files(directory: Path | None = None):
    if directory is None:
        directory = Path.cwd()

    sentences = []

    for txt_file in sorted(directory.glob("*.txt")):
        content = txt_file.read_text(encoding="utf-8").strip()
        sentence = Sentence(content)
        sentence.add_objects_add_next()
        sentences.append(sentence)

    return sentences


sentences = create_sentences_from_txt_files()
