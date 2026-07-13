marks = list(map(int, input("enter the studnet  marks : ").split()))
n = len(marks)

for i in range(n):
    for j in range(n - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

print("marks in ascending order : ")
print(marks)

