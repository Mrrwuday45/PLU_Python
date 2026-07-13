product_ids = list(map(int, input("enter product IDs (sorted) : ").split()))

target = int(input("enter product ID to search: "))

low = 0
high = len(product_ids) - 1

while low <= high:
    mid = (low + high) // 2

    if product_ids[mid] == target:
        print("Product Found at index:", mid)
        break
    elif product_ids[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Product Not Available")