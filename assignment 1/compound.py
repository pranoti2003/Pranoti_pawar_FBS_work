p=int(input("enter principle amount ="))
year=int(input("enter no.of years ="))
rate=float(input("enter rate of interest"))
compoundinterest =p*(1+(rate/year))**(year*rate)
print("compound interest is = ",compoundinterest )
