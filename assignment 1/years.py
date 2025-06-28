#to find years ,weeks and days from given no.days
days=int(input("enter no.of days ="))
years=days//365
days=days%365
weeks=days//7
days=days%7
print("years=",years,"weeks =",weeks,"days =",days)