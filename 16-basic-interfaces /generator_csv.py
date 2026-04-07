import csv

def csv_reader(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            yield line


# using generators in a loop
for row in csv_reader("example.csv"):
    print(row)

print()
print("-" * 100)
print()

# using next()
csv_gen = csv_reader("example.csv")
print("First row:\t", next(csv_gen))
print("Second row:\t", next(csv_gen))
print("Third row:\t", next(csv_gen))