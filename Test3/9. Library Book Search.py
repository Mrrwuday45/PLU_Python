book = list(range(10000,12000))
book_id = int(input("enter book id to search: "))

low = 0
high = len(book) - 1
found = False
while low <= high:
    mid = (low+high) // 2

    if book[mid] == book_id:
        print("Book found at position:", mid)
        found = True
        break
    elif book[mid] < book_id:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Book Not Found")


