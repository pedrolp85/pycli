class NumberLinesFilter(Filter):

    def __init__(self, stream: Iterator[str], num_lines: int) -> None:
        super().__init(stream)
        self._num_lines = num_lines


    def get_lines(self) -> Iterator[str]:
        counter = self._num_lines
        while counter > 0:
            yield next(self.stream)
            counter = counter - 1
