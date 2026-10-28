# 30. Store patient names and ages. Add, delete, search, display and count patients.

names = ["Amit", "Riya"]
ages = [20, 25]

names.append("Sneha")
ages.append(22)

names.remove("Riya")
ages.pop(1)

name = input("Search patient: ")
print("Found:", name in names)

print("Patients:", names)
print("Ages:", ages)
print("Total patients:", len(names))