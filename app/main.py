from input import get_input

import fileinput
from pathlib import Path

if __name__ == "__main__":

    path = Path(__file__).parent / "tests/unit/input/fixtures/example.txt"
    
    for a in get_input(file_path=path, file_reversed=True).get_lines():
       print(a)

