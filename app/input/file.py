from io import StringIO, SEEK_END
from pathlib import Path
from typing import Iterator, TextIO

class FileInput:

    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def get_lines(self):
        with open(self._file_path, "r") as file:
            line = "start"
            while line:
                line = file.readline()
                if line:
                    yield line.rstrip("\n")

class ReverseFileInput:

    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def get_lines(self):
        buffer = 100
        with open(self._file_path, "r") as file:
            file_end_pos = file.seek(0, SEEK_END)
            revlinebuf = StringIO()
            chunk_buf = StringIO()
            last_chunk_start = file_end_pos + 1
            while last_chunk_start > 0:
                if buffer > last_chunk_start:
                    buffer = last_chunk_start
                chunk_start = last_chunk_start - buffer
                file.seek(chunk_start)
                chunk_buf.write(file.read(buffer))
                chunk = chunk_buf.getvalue()
                while chunk:
                    lhs, separator_match, rhs = chunk.rpartition("\n")
                    if separator_match:
                        if rhs:
                            revlinebuf.write(rhs[::-1])
                        completed_line = revlinebuf.getvalue()[::-1]
                        revlinebuf.seek(0)
                        revlinebuf.truncate()
                        yield completed_line
                    else:
                        revlinebuf.write(chunk_buf.getvalue()[::-1])
                    chunk_buf.seek(len(lhs))
                    chunk_buf.truncate()
                    chunk = chunk_buf.getvalue()
                last_chunk_start = chunk_start
            completed_line = revlinebuf.getvalue()[::-1]
            yield completed_line


