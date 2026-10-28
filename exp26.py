# 26. Store marks of 20 students and find highest, lowest, average, above-average and below-average students.

marks = []

for i in range(20):
    marks.append(int(input("Enter marks: ")))

avg = sum(marks) / 20

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", avg)
print("Above average:", sum(x > avg for x in marks))
print("Below average:", sum(x < avg for x in marks))