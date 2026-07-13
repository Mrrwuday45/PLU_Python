marks = list(map(int, input("enter the marks of 50 students: ").split()))
marks.sort()

search_mark = int(input("enter mark to search: "))
low = 0
high = len(marks) - 1
found = False
while low<=high:
    mid = (low+high) // 2
    if marks[mid] == search_mark:
      print("marks found at position : ",mid)
      found = True
      break
    elif marks[mid] < search_mark:
       low = mid + 1
    else:
       high =  mid - 1
if not found:
    print("Mark Not Found")
print("sorted marks: ")
print(marks) 
         


