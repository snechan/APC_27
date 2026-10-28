# 19. Store names of students present in class. Display total students, search student, add student and remove an absent student.

students = ["Pranjali", "Prabha", "Sneha"]
print("Total students:", len(students))
name = input("Search student: ")
print(name in students)
students.append("Anjali")
students.remove("Sneha")
print("Students:", students)