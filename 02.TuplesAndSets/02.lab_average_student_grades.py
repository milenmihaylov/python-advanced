from statistics import mean

students = {}
for _ in range(int(input())):
    student, grade = input().split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for name in students.keys():
    print(f"{name} -> {' '.join([str(num)[0]+str(num)[1:].ljust(3,'0') for num in students[name]])} (avg: {mean(students[name]):.2f})")
