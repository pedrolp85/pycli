from abc import ABCMeta, abstractmethod

class Filter(metaclass=ABCMeta):

    def __init__(self, stream: Iterator[str]) -> None:
        self._stream = stream

    @abstractmethod
    def get_lines(self) -> Iterator[str]:
        pass