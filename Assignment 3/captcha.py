import random
userid=input("Enter userid =")
pass1=input("Enter passward =")

if(userid=="FBS"and pass1=="p123"):
    captcha=random.randint(1000,9999)
    print("captcha :",captcha)
    input=int(input("Enter captcha ="))
    if(input==captcha):
        print("Successful login ") 
    else:
     print("unsuccesful login ")
    
else:
    print("credentials are wrong unsuccessful login")
    