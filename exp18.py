employees = [("Amit", "IT", 60000), ("Riya", "HR", 40000)]

print(list(filter(lambda x: x[2] > 50000, employees)))
print(list(map(lambda x: (x[0], x[1], x[2] * 1.1), employees)))
print(sorted(employees, key=lambda x: x[2]))