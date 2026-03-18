file_name = input("Enter a file name: ")

lines = list()
with open(f"{file_name}.txt", mode="a") as f:
    while True:
        line = input("Enter a line [type END to finish): ")
        if line.upper() == "END":
            break
        line += "\n"
        lines.append(line)
    f.writelines(lines)