from typing import Optional
from pathlib import Path

from .input import Input
from .stdin import StdinInput
from .file import FileInput, ReverseFileInput

def get_input(file_path: Optional[Path] = None, file_reversed: bool = False) -> Input:
    if file_path:
        return FileInput(file_path) if not file_reversed else ReverseFileInput(file_path)
    return StdinInput()

