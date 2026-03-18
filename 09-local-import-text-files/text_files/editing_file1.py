# edit file
file_name = input("Enter a file name: ")

lines = list()

# 1. read a file
with open(f"{file_name}.txt", mode="r") as f:
    # copy the file content to lines list
    for line in f:
        lines.append(line)

# display the file content
print("File content:")
for line in lines:
    print(line[:-1])

# 2. write new lines to a file (with old lines as well)
with open(f"{file_name}.txt", mode="w") as f:
    while True:
        line = input("Enter a line [type END to finish): ")
        if line.upper() == "END":
            break
        line += "\n"
        lines.append(line)
    f.writelines(lines)

# 3. modify any line
line_number = int(input("Which line would you like to modify?: "))
lines[line_number-1] = input(f"What should be in the line number {line_number}?: ") + "\n"

with open(f"{file_name}.txt", mode="w") as f:
    f.writelines(lines)