# Opening the file in read mode ('r')
with open("/home/vinay/Documents/Code/python_practice/File_Handling/example.txt", "r") as file:

    # Reading the entire file content
    content = file.read()
    print("Entire file content:")
    print(content)

    # Reset the file pointer to the beginning
    file.seek(0)

    # Reading the file Line by Line
    print("File content line by line:")
    for line in file:
        print(line.strip())