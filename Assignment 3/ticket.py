
a1=int(input("enter age ="))
a2=int(input("enter age ="))
a3=int(input("enter age ="))
a4=int(input("enter age ="))
a5=int(input("enter age ="))
amount=int(input("Enter amount ="))
fair=0

if(a1<12):
    fair+=amount-(amount*0.3)
elif(a1>59):
    fair+=amount*0.5
else:
    fair+=amount
    
if(a2<12):
    fair+=amount-(amount*0.3)
elif(a2>59):
    fair+=amount*0.5
else:
    fair+=amount
    
if(a3<12):
    fair+=amount-(amount*0.3)
elif(a3>59):
    fair+=amount*0.5
else:
    fair+=amount
    
if(a4<12):
    fair+=amount-(amount*0.3)
elif(a4>59):
    fair+=amount*0.5
else:
    fair+=amount
    
if(a5<12):
    fair+=amount-(amount*0.3)
elif(a5>59):
    fair+=amount*0.5
else:
    fair+=amount
    
print(fair)
    