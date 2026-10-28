employees = [
    {"id": 1, "name": "Amit", "dept": "IT", "salary": 30000},
    {"id": 2, "name": "Priya", "dept": "HR", "salary": 40000},
    {"id": 3, "name": "Rahul", "dept": "IT", "salary": 25000}
]

with open("employees.txt", "w") as f:
    for e in employees:
        f.write(
            f'{e["id"]},{e["name"]},{e["dept"]},{e["salary"]}\n'
        )

with open("employees.txt", "r") as f:
    employees = []
    for line in f:
        i, name, dept, salary = line.strip().split(",")
        employees.append({
            "id": i, "name": name,
            "dept": dept, "salary": float(salary)
        })

for e in employees:
    print(e)

highest = max(employees, key=lambda e: e["salary"])
print("Highest-paid employee:", highest["name"])

avg = sum(e["salary"] for e in employees) / len(employees)
print("Average salary:", avg)

limit = float(input("Enter salary limit: "))
for e in employees:
    if e["salary"] > limit:
        print(e["name"], e["salary"])