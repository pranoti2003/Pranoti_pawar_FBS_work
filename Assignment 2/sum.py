#sum of3 digit number 
num=int(input ("Enter number ="))
a=num%10
num=num//10
b=num%10
c=num//10
sum=a+b+c
print("Sum of 3 digit number is =",sum)