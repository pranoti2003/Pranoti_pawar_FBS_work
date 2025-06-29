#swap two numbers using third variable
num1=int(input("enter num1 ="))
num2=int(input("enter num2 ="))
temp=num1+num2
num1=temp-num1
num2=temp-num2
print("After swapping numbers =")
print("num1 =",num1)
print ("num2 =",num2)
