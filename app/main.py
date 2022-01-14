from input.file import ReverseFileInput

if __name__ == "__main__":

    path = "example.txt"
    file_example = ReverseFileInput(path)
    #print(file_example)
    #print(file_example.next_line())
    for a in file_example.get_lines():
        print(a)
    
