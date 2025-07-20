s1=int(input("Enter marks ="))
s2=int(input("Enter marks ="))
s3=int(input("Enter marks ="))
s4=int(input("Enter marks ="))
s5=int(input("Enter marks ="))
total=s1+s2+s3+s4+s5
per=(total/500)*100
if(per>=80 and per<100):
    print("Distinction")
elif(per>=70 and per<80):
    print("First class")
elif(per>=60 and per<70):
    print("Second class")
elif(per>=50 and per<35):
    print("pass")
else:
    print("fail")
