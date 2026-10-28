def student(name, roll, marks):
    total = sum(marks)
    percentage = total / 5
    print(name, roll, total, percentage)

student("Amit", 1, [80, 70, 90, 85, 75])