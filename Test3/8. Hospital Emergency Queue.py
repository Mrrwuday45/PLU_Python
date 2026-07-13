patients = list(map(int, input("enter patient priority levels: ").split()))

patients.sort(reverse=True)

print("Emergency Queue:")
print(patients)