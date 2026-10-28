students = [("Amit", 80), ("Riya", 90), ("Raj", 60)]

marks = list(map(lambda x: x[1], students))
print(sum(marks) / len(marks))
print(list(filter(lambda x: x[1] > 75, students)))
print(sorted(students, key=lambda x: x[1]))