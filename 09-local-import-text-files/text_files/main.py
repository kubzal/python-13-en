
fd = open("example.txt")
print(fd.read(), type(fd.read()))
fd.close()

print()

fd = open("example.txt")
print(fd.readline()[:-1])
print(fd.readline()[:-1])
fd.close()

print()

fd = open("example.txt")

for index, line in enumerate(fd):
    print(f"[{index+1}] {line[:-1]}")

fd.close()

# THIS IS PREFERABLE WAY OF WORKING WITH TEXT FILES
print("\nWITH INSTRUCTION:\n")

with open("example.txt", "r") as fd:
    for line in fd:
        print(line[:-1])

# writing a file
file_name = input("Enter a file name: ")
with open(f"{file_name}.txt", mode="w") as f:
    lines = list()
    while True:
        line = input("Enter a line [type END to finish): ")
        if line.upper() == "END":
            break
        line += "\n"
        lines.append(line)
    f.writelines(lines)