side1=int(input("Enter side1 ="))
side2=int(input("Enter side2 ="))
side3=int(input("Enter side3 ="))
if(side1==side2==side3):
    print("Equilateral traiangle ")
elif(side1==side2!=side3):
    print("Isosceles triangle ")
else:
    print("Scalen triangle")