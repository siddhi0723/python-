#Writing data to a file (creates new file or overwrites if exists)
with open("assignment11.txt", "w") as file:
    file.write("This is assignment 11.\n")
    file.write("This assignment 11 is  of file handling.\n")

# Reading the file
with open("assignment11.txt", "r") as file:
    content = file.read()
    print("Reading file:")
    print(content)

# Appending new content to the file
with open("assignment11.txt", "a") as file:
    file.write("This line was appended again.\n")

# Reading again
with open("assignment11.txt", "r") as file:
    updated_content = file.read()
    print("\nAfter appending, file is :")
    print(updated_content)