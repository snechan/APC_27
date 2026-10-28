f = open("student.txt", "r")
lines = f.readlines()
print("Total number of lines:", len(lines))
f.close()