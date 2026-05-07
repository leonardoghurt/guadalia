from Debug import Debug
from pathlib import Path
Debug("aitrainer_script: pathlib module imported successfully")
from Sentence import Sentence
Debug("aitrainer_script: Sentence class imported successfully")

def create_sentences_from_txt_files(directory: Path | None = None):
    if directory is None:
        directory = Path.cwd()
    
    Debug(f"aitrainer_script: starting training from directory {directory.resolve()}")
    
    for txt_file in sorted(directory.glob("*.txt")):
        content = txt_file.read_text(encoding="utf-8").strip()
        Debug(
            f"aitrainer_script: loaded '{txt_file.name}' with "
            f"{len(content)} characters"
        )
        sentence = Sentence(content)
        Debug(f"aitrainer_script: created Sentence object for '{txt_file.name}'")
        sentence.add_objects_add_next()
        Debug(f"aitrainer_script: processed word transitions for '{txt_file.name}'")
        

Debug("aitrainer_script: running create_sentences_from_txt_files()")
sentences = create_sentences_from_txt_files()
