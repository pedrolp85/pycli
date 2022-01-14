from typing import Iterator
import fileinput

from .input import Input


class StdinInput(Input):
    
    def get_lines(self) -> Iterator[str]:
        for line in fileinput.input():
            yield line.rstrip("\n")