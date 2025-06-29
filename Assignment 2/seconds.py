#convert the time enterd in hh,min,sec into seconds
hour=int(input("enter hours = ")) 
min=int(input ("enter minutes ="))
sec=int(input("enter seconds ="))
totalseconds=hour*3600+min*60+sec 
print("Total seconds is =",totalseconds)