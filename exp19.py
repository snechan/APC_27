students = [
    ("Amit", 70, 100),
    ("Priya", 90, 100),
    ("Rahul", 60, 80)
]

with open("attendance.txt", "w") as f:
    for name, present, total in students:
        f.write(f"{name},{present},{total}\n")

with open("attendance.txt", "r") as f:
    for line in f:
        name, present, total = line.strip().split(",")
        percentage = int(present) / int(total) * 100

        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print(name, "has attendance below 75%.")