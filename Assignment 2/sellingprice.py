#calculate selling price of book based on cost price and discount
cp=int(input("Enter cost price = "))
discount=int(input("Enter discount ="))
sellingprice=cp*(1-discount/100)
print("Selling price of book is =",sellingprice)