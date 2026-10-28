# 27. Store salaries and find highest, lowest, average, employees above ₹50,000 and below ₹30,000.

salary = [25000, 35000, 55000, 60000, 28000]

print("Highest:", max(salary))
print("Lowest:", min(salary))
print("Average:", sum(salary) / len(salary))
print("Above 50000:", [x for x in salary if x > 50000])
print("Below 30000:", [x for x in salary if x < 30000])