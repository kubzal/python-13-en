import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "Warsaw"],
    ["Bob", 25, "Berlin"],
    ["Charlie", 35, "Paris"]
]

print(data)

with open("csv_example_file.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)