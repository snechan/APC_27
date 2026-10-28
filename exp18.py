def result(marks):
    p = sum(marks) / 5
    print("Percentage:", p)

    if p >= 75:
        print("Grade A")
    elif p >= 60:
        print("Grade B")
    elif p >= 40:
        print("Grade C")
    else:
        print("Fail")

result([80, 70, 90, 60, 85])