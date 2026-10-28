import csv

records = [
    [101, "Amit", 85],
    [102, "Priya", 92],
    [103, "Rahul", 78]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["RollNo", "Name", "Marks"])
    writer.writerows(records)

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    students = list(reader)

for s in students:
    print(s)

marks = [int(s["Marks"]) for s in students]
highest = max(students, key=lambda s: int(s["Marks"]))

print("Highest marks:", highest["Name"], highest["Marks"])
print("Average marks:", sum(marks) / len(marks))

print("Students scoring above 80:")
for s in students:
    if int(s["Marks"]) > 80:
        print(s["Name"], s["Marks"])