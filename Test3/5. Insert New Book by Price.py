book_price = list(map(int, input("enter the soretd book new price: ").split()))
new_price = int(input("enter the new book price : "))
i = 0

while i < len(book_price) and book_price[i] < new_price:
    i += 1

book_price.insert(i, new_price)
print("updated new price : ")
print(book_price)



