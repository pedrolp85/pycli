from input.file import FileInput, ReverseFileInput

class TestFileInput:
    def test_get_lines(self, mock_file, file_lines) -> None:
        file_input = FileInput("some_path.txt")
        result = list(file_input.get_lines())
        assert result == file_lines

class TestReversFileInput:
    def test_get_lines(self, mock_file, reverse_file_lines) -> None:
        file_input = ReverseFileInput("some_path.txt")
        result = list(file_input.get_lines())
        assert result == reverse_file_lines