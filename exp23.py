with open("file1.txt", "r") as f1:
    lines1 = f1.readlines()

with open("file2.txt", "r") as f2:
    lines2 = f2.readlines()

if lines1 == lines2:
    print("Both files are identical.")
else:
    print("Files are different.")

    for i in range(max(len(lines1), len(lines2))):
        line1 = lines1[i] if i < len(lines1) else "<No line>"
        line2 = lines2[i] if i < len(lines2) else "<No line>"

        if line1 != line2:
            print("First difference at line:", i + 1)
            print("File 1:", line1.strip())
            print("File 2:", line2.strip())
            break