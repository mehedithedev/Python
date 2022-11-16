print("Welcome to the Roller Coaster")
height=float(input("What's your height in feet? "))
if height>=5 :
    print("You are eligible to ride on the Roller Coaster!")
    age=int(input("How old are you? "))
    if age <= 12:
        print("You have to pay $5 to proceed further.")
    elif age <18:
        print("You have to pay $10. ")
    elif age <22:
        print("You have to pay $12")    
    else:
        print("You have to pay adult fees, which is $16 in order to proceed further.")
else:
    print("You have to wait more to achive the required height.")
