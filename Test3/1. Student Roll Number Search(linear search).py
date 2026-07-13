roll_numbers = list(map(int, input("enter the roll numbers : ").split()))
target = int(input("enter the roll number to search : "))

position = -1
for i in range(len(roll_numbers)):
    if roll_numbers[i] == target:
        position = i
        break

if position != -1:
    print("Student Found at position:", position + 1)

else:
    print("student not found")
    




 

