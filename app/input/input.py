from typing import Iterator
from abc import ABCMeta, abstractmethod

class Input(metaclass=ABCMeta):

    @abstractmethod
    def get_lines(self) -> Iterator[str]:
        pass


