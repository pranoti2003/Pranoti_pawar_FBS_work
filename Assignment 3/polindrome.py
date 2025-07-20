#program to check given 3 digit number is polindrome or not
num=int(input("Enter number ="))
copy=num
a=num%10
num=num//10
b=num%10
reverse=(a*10)+b
c=num//10
reverse=(reverse*10)+c
if(copy==reverse):
    print("Polindrome number")
else:
    print("Not Polindrome number")