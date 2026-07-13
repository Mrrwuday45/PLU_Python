timings = list(map(float, input("enter the partication timigs : ").split()))
n = len(timings)
for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if timings[j] < timings[min_index]:
            min_index = j

    timings[i], timings[min_index] = timings[min_index], timings[i]

print("timings from fastest to slowest:")
print(timings)

