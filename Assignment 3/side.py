a=int(input("enter side1 ="))
b=int(input("enter side2 ="))
c=int(input("enter side3 ="))

if(a+b>c)and(b+c>a)and(c+a>b):
    print("Triangle is valid ")
else:
    print("Triangle is not valid")