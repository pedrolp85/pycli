from input.file import ReverseFileInput
from input.stdin import StdinInput

import fileinput

if __name__ == "__main__":

    path = "example.txt"
    #file_example = ReverseFileInput()
    stdin_example = StdinInput()
    
    for a in stdin_example.get_lines():
       print(a)

