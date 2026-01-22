# Write a program that takes a student’s marks and prints whether they got “Distinction” (≥80), “Pass” (≥40), or “Fail” (<40).
marks = float(input("Enter student's marks: "))

if marks >= 80:
    print("Distinction")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")